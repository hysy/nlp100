# -*- coding: utf-8 -*-
import re
import load

title = "イギリス"
fn = "jawiki-country.json.gz"

def getAllMediaName(text):
    p = re.compile("ファイル:(.+?)\|")
    return [p.match(line).group(1)
            for line in text.splitlines() if p.match(line)]
    
text = load.load_text(fn, title)
print (getAllMediaName(text))
# print(type(text))
       
#for x in text:
#    print (type(x))


