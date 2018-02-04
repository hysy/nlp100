# import 20 ができなかったので load.py を作成した
import json
import gzip

fn = "jawiki-country.json.gz"
title = "イギリス"

def load_text(fn, title):
    ret = []
    with gzip.open(fn) as f:
#        print (f.decode('utf-8'))
        for line in f:
            data = json.loads(line.decode('utf-8'))
            # イギリスに関する記事は一記事だけだったので、見つかったらreturn
            if title == data['title']:
                 return data['text']
    
if __name__ == '__main__':    
    print(load_text(fn, title))
