import re
import load

title = "イギリス"
fn = "jawiki-country.json.gz"

def getTemplate(text):
    ret = {}
    begin = re.compile('\{\{基礎情報')
    end = re.compile('\}\}')
    hat = re.compile('\|(.+?)\s=\s(.+)')
    before_ref = re.compile('(.*?)<ref')
    rstrip_br = re.compile('(.*?)<br')

    data_flag = False
    for line in text.splitlines():
        if data_flag:
            if end.match(line):
                break
            if hat.match(line):
                key = hat.match(line).group(1)
                content = hat.match(line).group(2)
                if before_ref.match(content):
                    content = before_ref.match(content).group(1)
                if rstrip_br.match(content):
                    content = rstrip_br.match(content).group(1)
                ret[key] = content
        if begin.match(line):
            data_flag = True
    return ret


if __name__ == "__main__":
    text = load.load_text(fn, title)
    print (getTemplate(text))



