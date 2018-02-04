# -*- coding: utf-8 -*-
# import 20 ができなかったので load.py を作成した
import json
import gzip

fn = u"jawiki-country.json.gz"
title = u"イギリス"

def load_text(fn, title):
    with gzip.open(fn) as f:
        print (f)
        for line in f:
            data = json.loads(line.decode('utf-8'))
            if title == data['title']:
                return data['text']

print(load_text(fn, title))
