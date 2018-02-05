from matplotlib import pyplot
import numpy as np
import math

from ex30 import load_mecab
from ex36 import getFreqRank

fn = 'neko.txt.mecab'

def printloglogGraph(rank_list):
    freq_list = [v[1] for v in rank_list]

    pyplot.plot(freq_list)
    
    pyplot.title("Rank-Frequency loglogGraph")
    pyplot.ylabel("Frequency")
    pyplot.xlabel("Rank")

    pyplot.yscale("log")
    pyplot.xscale("log")
    
    pyplot.show()
    
    

if __name__ == "__main__" :
    dic = load_mecab(fn)
    rank_list = getFreqRank(dic)
    printloglogGraph(rank_list)
    
