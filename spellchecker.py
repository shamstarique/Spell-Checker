import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import wordnet as wn
from nltk.corpus import words
import re
import time

def edit_dist_1(word):
    "All edits that are one edit away from `word`."
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)


start_time = time.time()
print("\nText to Check: \n")
filename = "mobydick.txt"
file = open(filename, "r");
text = file.read() #load whole text file into one string
file.close()

#tokens = re.split('\s|(?<!\d)[,.](?!\d)', sentence) #tokenize the string
tokens_list = re.split('[ ,".)(;!?\n\t:-]',text) # creating a list of tokens

print("\n# of words in text: ")
print(len(tokens_list))


#putting tokens in a dictionary to get rid of duplicates
tokens_dict = {}
for token in tokens_list:
    tokens_dict[token.lower()] = token.lower()



print("\n# of tokens from text(removed duplicates): ")
print(len(tokens_dict))

misspelled_words_list = []

#create a python dictionary of the english dictionary from nltk words and wordnet
dict_list_words = words.words()


dictionary = {}
file = open("our_dictionary.txt", "r");
dictionary_textfile = file.read() #load whole text file into one string
words_in_dict = re.split('\n', dictionary_textfile)
file.close()

for word in words_in_dict:
    dictionary[word] = word
    dictionary[word.lower()] = word.lower()
for token in tokens_dict:
    if(not (token in dictionary)):
        if(not (token.lower() in dictionary)):
            misspelled_words_list.append(token)


#Spellchecker
for token in tokens_dict:
    if(not (token in dictionary)):
        misspelled_words_list.append(token)


#tokens = nltk.word_tokenize(sentence)
print("\n# of misspelled words: ")
print(len(misspelled_words_list))
print("\nMisspelled words :")
print(misspelled_words_list)



#print(wn.synsets('cannonball'))
#print("cannonball" in words.words())

#part 2: misspelled word correction. Give suggestsion for the misspelled words

for word in misspelled_words_list:
    suggested_words = 0;
    print()
    print(word, end='')
    print(": ", end='')
    word_1_edit_dist_away = edit_dist_1(word)
    for word2 in word_1_edit_dist_away:
        if suggested_words >= 3:
            break
        if word2 in dictionary:
            print(word2, end='')
            print(", ", end='')
            suggested_words +=1
        if suggested_words < 3 :
            word_2_edit_dist_away = edit_dist_1(word2)
            for word3 in word_2_edit_dist_away:
                if word3 in dictionary:
                    if suggested_words >= 3:
                        break
                    print(word3, end='')
                    print(", ", end='')



end_time = time.time()
print("\nTime to finish: ")
print(end_time - start_time)
