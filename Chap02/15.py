import sys

args = sys.argv
N = int(args[1])

with open("hightemp.txt") as f:
    lines = f.readlines()
    for line in lines[-N:]:
        print(line.rstrip())
    

