import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import wordnet as wn
from nltk.corpus import words
import re
import time


start_time = time.time()
print("\nText to Check: \n")
filename = "mobydick.txt"
file = open(filename, "r");
text = file.read() #load whole text file into one string

#tokens = re.split('\s|(?<!\d)[,.](?!\d)', sentence) #tokenize the string
tokens_list = re.split('[ ,".;!?\n\t:-]',text) # creating a list of tokens

print("\n# of words in text: ")
print(len(tokens_list))


#putting tokens in a dictionary to get rid of duplicates
tokens_dict = {}
for token in tokens_list:
    tokens_dict[token] = token

print("\n# of tokens from text(removed duplicates): ")
print(len(tokens_dict))

misspelled_words_list = []

#create a python dictionary of the english dictionary from nltk words and wordnet
dict_list_words = words.words()
dict_list_wordnet = wn.wn()

dictionary = {}
for word in dict_list_words:
    dictionary[word] = word
for word in dict_list_wordnet:
    dictionary[word] = word

for token in tokens_dict:
    if(not (token in dictionary)):
        #if(len(wn.synsets(token)) == 0):
        misspelled_words_list.append(token)

"""
#Spellchecker
for token in tokens_dict:
    if(not (token in words.words())):
        if(len(wn.synsets(token)) == 0):
            misspelled_words_list.append(token)

"""
#tokens = nltk.word_tokenize(sentence)
print("\n# of misspelled words: ")
print(len(misspelled_words_list))
print("\nMisspelled words :")
print(misspelled_words_list)


end_time = time.time()
print("\nTime to finish: ")
print(end_time - start_time)


#print(wn.synsets('cannonball'))
#print("cannonball" in words.words())