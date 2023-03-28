# GTE2 Translation

This repository contains automatically English translated FTB Quests configurations for [\[GTCEu\] GregTech Expert 2](https://www.curseforge.com/minecraft/modpacks/gregtech-expert-2) made with DeepL. Also provides a simple automation script not specific to GTE2.

### How to use

- Download the latest release from the releases page (or the one corresponding with your GTE2 version)
- Drag and drop the `config` folder in your Minecraft instance folder
- Greg out in (slightly broken?) English!

### Running the script

For this you're going to need a [DeepL](https://www.deepl.com) account. The entirety of the questbook as of writing this is around ~120k characters, so it comfortably fits in the monthly DeepL free tier quota.
```
$ mv /path/to/your/ftbutils .
$ pip3 install -r requirements.txt
$ DEEPL_AUTH_KEY="<insert your deepl key here>" python3 translate.py
$ mv ftbutils-tl /path/to/your/ftbutils
```

To update certain quests without having to re-translate everything (which takes quite a bit), simply delete them from the `ftbutils-tl` folder and run the script again.

### Known issues

- Translation *might* break formatting codes from within the contents of the quests
