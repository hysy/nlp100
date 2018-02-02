# 任意の（文字|単語）を連続したN個で区切る
# 今回はN=2のみ
s = "I am an NLPer"

def n_gram(lst, N):
    dic = {}
    for idx in range(len(lst)-N+1):
        text = tuple(lst[idx:idx+N])
        if text in dic.keys():
            dic[text] += 1
        else :
            dic[text] = 1
    return dic
            

print(n_gram(s, 2))
print(n_gram(s.split(), 2))
