import re
from ex50 import getSentenceList

fn = 'nlp.txt'

def getWordsList(sentence_list):
    return [[re.sub('[^a-zA-Z0-9]', '', word) for word in sentence.split()] for sentence in sentence_list]

if __name__ == '__main__':
    with open(fn) as f:
        data = f.read()
        sentence_list = getSentenceList(data)
        for sentence in getWordsList(sentence_list):
            for word in sentence:
                print(word)
            print()

