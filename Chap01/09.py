import random

s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

def ex_shuffle(s):
    words = s.split()
    ret = []
    for word in words:
        if len(word) <= 4:
            ret.append(word)
        else :
            shuffled_list = [c for c in word[1:-1]]
            random.shuffle(shuffled_list)
            ret.append(word[0] + "".join(shuffled_list) + word[-1])
    return ret
print (ex_shuffle(s))
