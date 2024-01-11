# 2. Demonstrate word stemming using Regular Expression, Porter Stemmer and Lancaster Stemmer and report the output. (6 marks)

import re
from nltk.stem import PorterStemmer, LancasterStemmer
from nltk.tokenize import word_tokenize

#Load the data
with open("Assignment Data\\Data_1.txt", "r") as file:
    data = file.read()

tokens = word_tokenize(data)

def stem(word):
    regexp = r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)?$'
    stem, suffix = re.findall(regexp, word)[0]
    return stem

porter = PorterStemmer()
lancaster = LancasterStemmer()

print ("RE Stemmer output : ")
print([stem(t) for t in tokens])
print("\n")

print ("Porter Stemmer output : ")
print([porter.stem(words) for words in tokens])
print("\n")

print ("Lancaster Stemmer output : ")
print([lancaster.stem(words) for words in tokens])
