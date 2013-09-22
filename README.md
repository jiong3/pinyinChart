# Pinyin Chart

License: [CC BY-NC-SA 3.0](http://creativecommons.org/licenses/by-nc-sa/3.0/)

[pdf releases](https://github.com/jiong3/pinyinChart/releases)

![Preview](https://github.com/jiong3/pinyinChart/releases/download/v1.0/traditional.png)

This is a printable "map" of all the sounds used in Mandarin Chinese. The minimum size of a printout should be A3. For every item it shows the complete pinyin and an example character along with the tone and the meaning of the character. All definition keywords are unique. Around each character there is a ring with four segments, one for each tone (NW: 1, NE: 2, SW: 3, SE: 4). The more characters use the sound with this tone, the darker the segment is. If no character has this pronunciation, the segment is missing. The neutral tone is ignored.

## Purpose

Apart from hanging it on the wall this can be used for:
-  teaching pinyin to native Chinese who only know the characters (probably not very common in Mainland China...)
-  creating mnemonics with the keywords. The idea is that if you can't remember a pronunciation of a character, lets say 貨 (huo4), you can think of a simple character you already know (火 "fire"）with the same pronunciation. If you connect 貨 and other characters with the same pronunciation with "fire" using mnemonics you have an additional help for remembering the pronunciation. For the tone you would need an additional technique, like colors or other mnemonic tricks. The pinyin map provides a keyword for all the Chinese sounds, so that you can use it for all the characters you might want to learn.

## Editing

Feel free to create your own version! It is recommended to use [Inkscape](http://www.inkscape.org) for editing the svg file.
It's really easy to change fonts and move everything around since the file is organized in layers. Those are all locked by default, so without the layer dialog you won't be able to change anything.

### Fonts
For the Chinese characters [DroidSans](https://github.com/android/platform_frameworks_base/blob/master/data/fonts/DroidSansFallbackFull.ttf?raw=true) (click Raw to download) is used, for everything else the [Ubuntu font family](http://font.ubuntu.com/).

### Scripts
In the helpers directory there are some python3 scripts which might be helpful. These depend on the structure of the file, so any major editing of the file (deleting layers or items) will not be compatible. You might need to change the path constants in the beginning of each script if your filenames are different.

- addFrequency.py + prons8000.txt: Add the frequency ring to all characters
- getKeywords.py: Generate a keywords text file from the svg
- setKeywords.py: Edit the keywords text file and use this script to put the changes back into the svg.
- tradToSimp.py + tradToSimp.txt: Use it to convert all traditional characters to simplified ones, but please pay attention to the output of the script, if it says "please edit ..." you have to edit this one in the svg file to choose which simplified character you would like to have. Also, if you want to be 100% sure the conversion is correct you should check all characters by yourself.
