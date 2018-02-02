lst = []
with open("hightemp.txt") as f:
    lines = f.readlines()
    for line in lines:
        lst.append((float(line.split()[2]), line))

lst = sorted(lst)
for x in lst:
    print(x[1].rstrip())
