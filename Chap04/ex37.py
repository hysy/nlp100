from matplotlib import pyplot

from ex30 import load_mecab
from ex36 import getFreqRank

fn = 'neko.txt.mecab'

def printTopNList(rank_list, N):
    horizontal_list = []
    vertical_list = []
    count = 0
    for key, value in rank_list: 
        print (str(key) + ' ' + str(value))
        horizontal_list.append(key)
        vertical_list.append(value)
        count += 1
        if count == N:
            break
    pyplot.title("Word Frequency Top " + str(N))
    pyplot.ylabel("Frequency")
    pyplot.xlabel("Word")
    pyplot.bar(range(1, N+1), vertical_list)
    pyplot.xticks(range(1, N+1), horizontal_list)
    pyplot.show()
    
    

if __name__ == "__main__" :
    dic = load_mecab(fn)
    rank_list = getFreqRank(dic)
    printTopNList(rank_list, 10)
    
