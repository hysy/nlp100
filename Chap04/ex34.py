from ex30 import load_mecab

fn = 'neko.txt.mecab'


def joined_no(dic):
    ret = []
    for line_dic in dic:
        if len(line_dic) >= 3:
            for no in range(1, len(line_dic)-1):
                if line_dic[no]['surface'] == 'の':
                    if line_dic[no-1]['pos'] == line_dic[no+1]['pos'] and line_dic[no+1]['pos'] == '名詞':
                        ret.append(line_dic[no-1]['surface'] + "の" + line_dic[no+1]['surface'])
    return ret


if __name__ == "__main__" :
    dic = load_mecab(fn)
    print (joined_no(dic))
    
