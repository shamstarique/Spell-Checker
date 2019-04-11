import re
from nltk.corpus import words



file = open("filenames.txt", "r");
text1 = file.read() #load whole text file into one string
filenames = re.split('\n', text1)
file.close()



#create a python dictionary of the english dictionary from nltk words and wordnet
dict_list_words = words.words()
dictionary = {}
for word in dict_list_words:
    dictionary[word] = word

print(len(dictionary))

for filename in filenames:
   # filename_str = "C:\Users\Tarique\Downloads\scowl-2018.04.16\final" + filename
    file = open(filename, "r");
    text = file.read()  # load whole text file into one string
    file.close()
    tokens = re.split('\n', text) #tokenize the string
    for token in tokens:
        dictionary[token] = token

#tokens_list = re.split('[ ,".;!?\n\t:-]',text) # creating a list of tokens

print(len(dictionary))
print(dictionary)

f =open("our_dictionary.txt", "w")
for word in dictionary:
    f.write(word)
    f.write("\n")

f.close()
