import re

fn = 'nlp.txt'

def getSentenceList(plain):
    sentence_reg = re.compile('([.;:?!])\s([A-Z])')
    # 改行をスペースに
    stream = re.sub('(\s*\n+)+\s*', ' ', plain)

    # 区切り文字（文の最初の文字） + 区切り抜き文 +  区切り文字（文の最後の文字）
    # 最初は検知されないのでダミーを付ける
    tmp = []
    tmp.append("")
    for s in sentence_reg.split(stream):
        tmp.append(s)
    tmp.append("")
    
    return ["".join(tmp[3*i:3*(i+1)]) for i in range(len(tmp) // 3)]

if __name__ == '__main__':
    with open(fn) as f:
        data = f.read()
        for line in getSentenceList(data):
            print(line)
