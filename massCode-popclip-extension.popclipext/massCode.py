#!/usr/bin/env python3.8

import os
import time
import requests
import logging

# src format: https://github.com/yoeo/guesslang
# dst format: https://github.com/massCodeIO/massCode/blob/e884d706468e455cf4ad9be65e43c82d50bb37e0/src/renderer/components/editor/languages.ts#L86
remap_lang = {
    "go": "golang",
    "shell": "sh",
}

masscode_api = "http://127.0.0.1:3033"
logging.basicConfig(filename="/tmp/masscode_popclip.log", level=logging.INFO)


def guess_language(text):
    try:
        from guesslang import Guess

        guess = Guess()
        lang = guess.language_name(text).lower()
        if lang in remap_lang:
            lang = remap_lang[lang]
        logging.info(f"Detected language: {lang}")
        return lang
    except ImportError:
        return "plaintext"


def get_lang_tags(lang):
    try:
        tags = requests.get(
            f"{masscode_api}/tags",
        ).json()
        for tag in tags:
            if tag["name"] == lang:
                return tag["id"]
    except Exception:
        pass
    return None

def create_snippet(text):
    lang = guess_language(text)
    name = time.strftime("%Y-%m-%d %H:%M:%S")
    payload = {
        "name": name,
        "content": [
            {
                "value": text,
                "language": lang,
                "label": "Fragment 1",
            }
        ],
    }

    # TODO: support auto lang tag
    # currently it seems that due to masscode's tag system, it's not possible to create a tag on the fly
    # if lang != "plaintext":
    #     tag_id = get_lang_tags(lang)
    #     if tag_id:
    #         payload["tagsIds"] = [
    #             tag_id,
    #         ]

    resp = requests.post(
        f"{masscode_api}/snippets/create",
        json=payload,
    )

    logging.error(f"Failed to create snippet: {resp.text}")
    logging.error(f"Payload: {payload}")


if __name__ == "__main__":
    popclip_text = os.environ["POPCLIP_TEXT"]
    create_snippet(popclip_text)
