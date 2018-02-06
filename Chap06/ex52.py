import re
from nltk import stem

from ex50 import getSentenceList
from ex51 import getWordsList

fn = 'nlp.txt'

def stemWordsList(words_list):
    return [[(word, stem.PorterStemmer().stem(word)) for word in words] for words in words_list ]

if __name__ == '__main__':
    with open(fn) as f:
        data = f.read()
        sentence_list = getSentenceList(data)
        word_list = getWordsList(sentence_list)
        stemmed_list = stemWordsList(word_list)
        
        for words in stemmed_list :
            for word in words :
                print (word)
            print()
        
