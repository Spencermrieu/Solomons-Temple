import random



#Generate random number between 1 - 7
sentance_length = random.randrange(1,7)

print("And God Said:")

for xrange in range(sentance_length):


    #Generate random number between 1 - 58110
    word_selection = random.randrange(1,58110)
    #print(word_selection)

    #Pick a word from the english library
    lines = [] #Declare an empty list named "lines"
    with open ('corncob_lowercase.txt', 'rt') as in_file:  #Open file corncob_lowercase.txt for reading of text data.
        for line in in_file: #For each line of text store in a string variable named "line", and
            lines.append(line)  #add that line to our list of lines.

    #print(lines)        #prints the list of all object.
    #print(lines[word_selection])
    print(lines[word_selection].rstrip())
