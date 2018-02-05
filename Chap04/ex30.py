# http://taku910.github.io/mecab/#usage-tools とかを見ると
# 表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音
# の用になっている

fn = 'neko.txt.mecab'

def load_mecab(fn):
    keys = ['surface', 'pos', 'pos1', 'pos2', 'pos3', 'infection',
            'conjugations', 'base', 'read', 'pronunciation']
    
    with open(fn) as f:
#               # 単語をkeysで表現
        return [[dict(zip(keys, word.replace('\t', ',').split(',')))
                # 改行で単語毎
                     for word in line.split('\n') if word!='']
                # End Of Sentence までで1文
                for line in f.read().split('EOS\n') if line != '']

if __name__ == '__main__':
    print(load_mecab(fn))
