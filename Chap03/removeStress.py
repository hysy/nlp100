import re

import load
import template


title = "イギリス"
fn = "jawiki-country.json.gz"

def removeStress(dic):
    r = re.compile("'+")
    return {key: r.sub('', value) for key, value in dic.items()}


if __name__ == "__main__":
    text = load.load_text(fn, title)
    template = template.getTemplate(text)
    # stressed = removeStress(template)
    print (removeStress(template))
