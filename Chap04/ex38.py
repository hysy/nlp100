from matplotlib import pyplot
import numpy as np
import math

from ex30 import load_mecab
from ex36 import getFreqRank

fn = 'neko.txt.mecab'

def printHistgram(rank_list):

    freq_list = [v[1] for v in rank_list]
    pyplot.hist(freq_list, range=(np.min(freq_list), np.max(freq_list)), log=True)
    
    pyplot.title("Word Frequency Histgram")
    pyplot.ylabel("Frequency")
    pyplot.xlabel("Word")

    pyplot.show()
    
    

if __name__ == "__main__" :
    dic = load_mecab(fn)
    rank_list = getFreqRank(dic)
    printHistgram(rank_list)
    
