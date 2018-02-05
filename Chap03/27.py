import re

import load
import template
import removeStress


title = "イギリス"
fn = "jawiki-country.json.gz"

def removeInnerLinks(dic):
    ret = {}
    r = re.compile('\[\[(.+\||)(.+?)\]\]')
    for key, value in dic.items():
        ret[key] = r.sub(r'\2', value)
    return ret


if __name__ == "__main__":
    text = load.load_text(fn, title)
    template = template.getTemplate(text)
    removed_stress = removeStress.removeStress(template)
    # print (removed_stress)
    print (removeInnerLinks(removed_stress))
