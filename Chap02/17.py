dic = {}

with open("hightemp.txt") as f:
    lines = f.readlines()
    for idx, line in enumerate(lines):
        dic[line.split()[0]] = 1
for key in dic.keys():
    print(key)
