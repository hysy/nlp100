import sys
from xml.etree import ElementTree 

fn = 'nlp.txt.xml'

if __name__ == "__main__":
    root = ElementTree.parse(fn).getroot()
    word_list = root.findall('.//word')

    for word in word_list:
        print(word.text)
