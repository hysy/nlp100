from collection import Counter

with open("hightemp.txt") as f:
    lines = f.readlines()
    counter = Counter([line.split()[0] for line in lines])

    for word, count in counter.most_common():
        print (word + ":\t" + count)
    
