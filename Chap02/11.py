with open("hightemp.txt") as f:
    lines = f.readlines()
    for line in lines:
        print(line.replace('\t', ' '), end='')
