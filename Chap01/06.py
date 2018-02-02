
def n_gram(lst, N):
    dic = {}
    for idx in range(len(lst)-N+1):
        text = tuple(lst[idx:idx+N])
        if text in dic.keys():
            dic[text] += 1
        else :
            dic[text] = 1
    return dic

para1 = "paraparaparadise"
para2 = "paragraph"

X = n_gram(para1, 2)
Y = n_gram(para2, 2)

# X∪Y
def dict_add(X, Y):
    dic = X.copy()
    for key, value in Y.items():
        if key in dic.keys():
            dic[key] += value
        else :
            dic[key] = value
    return dic

# X-Y
# Xから、XとYに含まれるものを除外
def dict_sub(X, Y):
    dic = {}
    for key, value in X.items():
        if not key in Y.keys():
            dic[key] = value
    return dic

# X∩Y
def dict_mul(X, Y):
    dic = {}
    for key, value in X.items():
        if key in Y.keys():
            dic[key] = value + Y[key]
    return dic

print("dict add")
print(dict_add(X, Y))

print("dict sub")
print(dict_sub(X, Y))

print("dict mul")
print(dict_mul(X, Y))

print("\'se\' in X?")
print(('s', 'e') in X)

print("\'se\' in Y?")
print(('s', 'e') in Y)


