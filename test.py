import re


file = open("filenames.txt", "r");
text = file.read() #load whole text file into one string
filenames = re.split('\n', text)


words_dict = {}

for filename in filenames:
    file = open(filename, "r");
    text = file.read()  # load whole text file into one string
    tokens = re.split('\n', text) #tokenize the string
    for token in tokens:
        words_dict[token] = token

#tokens_list = re.split('[ ,".;!?\n\t:-]',text) # creating a list of tokens

print(tokens)
"""