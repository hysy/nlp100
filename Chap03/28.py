import re

import load
import template
import removeStress as rS
import removeInnerLinks as rIL


title = "イギリス"
fn = "jawiki-country.json.gz"

def removeMarkup(dic):
    removed_stress = rS.removeStress(dic)
    removed_inner_links = rIL.removeInnerLinks(removed_stress)
    target = removed_inner_links
    ret = {}
    r = re.compile('\{\{(.+\||)(.+?)\}\}')
    for key, value in target.items():
        ret[key] = r.sub(r'\2', value)
    return ret


if __name__ == "__main__":
    text = load.load_text(fn, title)
    template = template.getTemplate(text)
    removed_markup = removeMarkup(template)
    print (removed_markup)
