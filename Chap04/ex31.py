from ex30 import load_mecab

fn = 'neko.txt.mecab'
def getMorphemeList(dic, key, value, morpheme):
    return [word_dic[morpheme]
           for sentence_dic in dic for word_dic in sentence_dic if word_dic[key] == value]

if __name__ == "__main__" :
    dic = load_mecab(fn)
    print (getMorphemeList(dic, 'pos', '動詞', 'surface'))
    
