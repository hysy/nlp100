import sys

args = sys.argv
N = int(args[1])

with open("hightemp.txt") as f:
    lines = f.readlines()
    LinesLen = len(lines)
    SectionLen = LinesLen // N
    for n in range(N):
        head = SectionLen * n
        tail = head + SectionLen if n != N-1 else LinesLen
        print("Section" + str(n) + ": ")
        for line in lines[head:tail]:
            print(line.rstrip())
        print()
