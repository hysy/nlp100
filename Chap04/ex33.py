from ex30 import load_mecab
from ex31 import getMorphemeList

fn = 'neko.txt.mecab'

if __name__ == "__main__" :
    dic = load_mecab(fn)
    print (getMorphemeList(dic, 'pos1', 'サ変接続', 'surface'))
    
