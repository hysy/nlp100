import re
import load

title = "イギリス"
fn = "jawiki-country.json.gz"

def getStressedContent(text):
    p = re.compile("'+")
    for line in text.splitlines():
#        print(line)
#        if p.match(line):
        print (p.sub('',line))
        
    return ""
text = load.load_text(fn, title)
# text = load.loads_text(fn, title)
print (getStressedContent(text))
