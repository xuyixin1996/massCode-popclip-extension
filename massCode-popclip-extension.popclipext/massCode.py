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

if __name__ == "__main__":
    logging.basicConfig(filename="/tmp/masscode_popclip.log", level=logging.INFO)
    # popclip_text = sys.stdin.read()
    popclip_text = os.environ["POPCLIP_TEXT"]
    lang = "plaintext"
    try:
        from guesslang import Guess

        guess = Guess()
        lang = guess.language_name(popclip_text).lower()
        if lang in remap_lang:
            lang = remap_lang[lang]
        logging.info(f"Detected language: {lang}")
    except ImportError:
        pass
    name = time.strftime("%Y-%m-%d %H:%M:%S")
    requests.post(
        "http://127.0.0.1:3033/snippets/create",
        json={
            "name": name,
            "content": [
                {
                    "value": popclip_text,
                    "language": lang,
                    "label": "Fragment 1",
                }
            ],
        },
    )
