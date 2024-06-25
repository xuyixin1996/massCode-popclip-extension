#!/bin/bash
# #popclip
# name: massCode
# icon: iconify:pajamas:snippet

# for testing, you can refer to the official document https://www.popclip.app/dev/shell-script-actions
name=$(date +%F_%T)

curl -X POST http://127.0.0.1:3033/snippets/create -H 'Content-Type: application/json' -d "{
  \"name\": \"${name}\",
  \"content\": [
    {
      \"label\": \"Fragment 1\",
      \"language\": \"plain_text\",
      \"value\": \"$POPCLIP_TEXT\"
    }
  ]
}"
