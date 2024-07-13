# massCode Popclip Extension

[massCode-popclip-extension](https://github.com/xuyixin1996/massCode-popclip-extension) is a [Popclip](https://pilotmoon.com/popclip/) extension to create snippets in [massCode](https://masscode.io/).

## Prerequisites

Currently this extension is only tested on macOS and use fixed python3.8 version and use `requests` to post snippets to
massCode.

```bash
brew install python@3.8
python3.8 -m pip install requests
```


We need [guesslang](https://github.com/yoeo/guesslang) to help detect the language of the code snippet.

```bash
git clone https://github.com/yoeo/guesslang.git
cd guesslang
git checkout dependabot/pip/tensorflow-2.11.1
python3.8 -m pip install .
```

## Installation

1. Download the `massCode.popclipext` in the git.
2. Double click on the `massCode.popclipext` file.
3. Click on the `Install` button.

## Usage

1. Select the text you want to create snippets.
2. Click on the `massCode` icon ![massCode](./logo.png =x15) and select the selected text will be stored in `massCode`
   snippets.

## Troubleshooting

If you have any issues with the extension, you can check the logs by running the following command:

```bash
tail -f /tmp/masscode_popclip.log
```

## Development

Check the [Popclip Extension Documentation](https://www.popclip.app/dev/packages) for more information.

## License

MIT
