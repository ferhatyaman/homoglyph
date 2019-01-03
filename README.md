# Homoglyph
Find homoglyph characters in two compared words. 

Main concern of this project is investigating whether a link behind the html href tag is diretcting a fake website using homoglyph conjugate or not.
However, if you want to use want use homoglyph comparator, you can implement your own reader and integrate with homoglyph comparator.

## Getting Started


In orthography and typography, a [homoglyph](https://www.wikiwand.com/en/Homoglyph) is one of two or more graphemes, characters, or glyphs with shapes that appear identical or very similar. The designation is also applied to sequences of characters sharing these properties.

**For example:** 

1. microsoft.com and rnicrosoft.com (m and rn)
2. flicker.com and fIicker.com (lowercase L and capital i. Looks almost same isn't it!?!)
### Prerequisites
1. Make sure your those python3 libraries in your lib file:
```python3
import urllib, html, json, homoglyph
```
2. There should be twitter data under ./txt file to read to run TwitterDataReader.py
3. confusables.txt contains all homoglyph conjugates which is needed to run homoglyph.py

### Running the process

1. Run directly main.py file to generate output.txt 
2. You can use homoglyph.py easily to compare your texts contains homoglyph caracters or not. 
