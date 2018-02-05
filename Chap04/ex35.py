from ex30 import load_mecab

fn = 'neko.txt.mecab'

def getConsecutiveNouns(dic):
    ret = []
    tmp = []
    for sentence_dic in dic:
        for word_dic in sentence_dic:
            if word_dic['pos'] == '名詞':
                tmp.append(word_dic['surface'])
            else:
                if (len(tmp) > 2):
                    ret.append(''.join(tmp))
                tmp = []
    return ret

if __name__ == "__main__" :
    dic = load_mecab(fn)
    print (getConsecutiveNouns(dic))
    
