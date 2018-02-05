# 以下を参照
# https://www.mediawiki.org/wiki/API:Main_page/ja
# https://www.mediawiki.org/wiki/API:Imageinfo
import re
import requests
import json

import load
import template

import removeMarkup as rM

title = "イギリス"
fn = "jawiki-country.json.gz"

def getFlagURL(dic):
    url_base = 'https://commons.wikimedia.org/w/api.php?'
    query = ('action=query&titles=File:' + dic['国旗画像'].replace(' ', '_')
             + '&prop=imageinfo&iiprop=url&format=json')
    url = url_base + query
    
    data = requests.get(url)
    json_data = json.loads(data.text)

    # "url":"(.+?)" したほうが早かったかも
    page_id = list(json_data['query']['pages'].keys())[0].rstrip()
    flag_url = json_data['query']['pages'][page_id]['imageinfo'][0]['url']
    
    return flag_url

if __name__ == "__main__":
    text = load.load_text(fn, title)
    template = template.getTemplate(text)
    removed_markup = rM.removeMarkup(template)
    flag_url = getFlagURL(removed_markup)
    print (flag_url)
