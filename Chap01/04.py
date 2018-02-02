# アルファベットにはピリオド、カンマも含める
s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
words = s.split()

indexes = [1, 5, 6, 7, 8, 9, 15, 16, 19]
prefix1 = [(words[idx-1][0], idx) for idx in indexes]
prefix2 = [(words[idx-1][:2], idx) for idx in range(1,21) if idx not in indexes]

dic = {x: y for (x,y) in prefix1 + prefix2}
print (dic)
