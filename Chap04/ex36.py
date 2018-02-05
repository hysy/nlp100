from collections import Counter
from ex30 import load_mecab

fn = 'neko.txt.mecab'

def getFreqRank(dic):
    word_counter = Counter([word_dic['base'] for sentence_dic in dic for word_dic in sentence_dic])
    return [(key, value) for key, value in word_counter.most_common()]

if __name__ == "__main__" :
    dic = load_mecab(fn)
    print (getFreqRank(dic))
    
