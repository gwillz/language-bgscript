language-bgscript
=================
Version: 0.5.0

Syntax highlighting for BGScript by [Bluegiga](https://www.bluegiga.com/en-US/).

Based on the Notepad++ highlighter provided by SiliconLabs and the `gecko.xml`
included in the BLE SDK.

Usage
-----
This package obviously includes a complete grammar, but also contains a parser
written in Python to scrape keywords from the Notepad++ highlighter and the
`gecko.xml`.

```sh
cd parse/
python3 scrape.py gecko.xml userDefineLang_BGScript.xml > ../grammars/bgscript.cson
```

Contributors
------------
+ [Gwilyn Saunders](https://git.gwillz.com.au/u/gwillz)

BGScript and associated trademarks belong to Bluegiga/SiliconLabs.
