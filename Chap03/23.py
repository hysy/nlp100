# -*- coding: utf-8 -*-
import re
# import 20
import load

title = "イギリス"
fn = "jawiki-country.json.gz"

def getAllCategory(text):
#     print (text.splitlines()[0])
#     print (text.splitlines()[1])
    p = re.compile("(^=+)(.*?)=+")
    return [(p.match(line).group(2), len(p.match(line).group(1))-1)
            for line in text.splitlines() if p.match(line)]
    
text = load.load_text(fn, title)
print (getAllCategory(text))
# print(type(text))
       
#for x in text:
#    print (type(x))


