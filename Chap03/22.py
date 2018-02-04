# -*- coding: utf-8 -*-
import re
# import 20
import load

title = "イギリス"
fn = "jawiki-country.json.gz"

def getAllCategory(text):
    p = re.compile("^\[\[Category:(.*?)(\|.*\]\]|\]\])")
    return [p.match(line).group(1) for line in text.splitlines() if p.match(line) ]
    
text = load.load_text(fn, title)
print (getAllCategory(text))
# print(type(text))
       
#for x in text:
#    print (type(x))


