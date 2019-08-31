import re
import sys

# opening input file to read from
input_file = open(sys.argv[1], "r")

# checking if that file can be read, terminates program if not
if not input_file.readable():

    print("File could not be opened. Please try running the program again with a valid file.")
    exit()

# initializing variable used to store current line being read (also used to terminate while-loop when string is empty)
current_line = "Dummy text"

# initializing global dictionary variable holding key-value pairs (where key = word and value = # of times word found)
word_dictionary = {}

# using while-loop to read file line by line until reaching end of file
while current_line != "":

    # reading line
    current_line = input_file.readline()

    # making list of words, excluding any punctuation or whitespace using regex
    word_list = re.split('\W+', current_line)

    # making entry in word_dictionary for every word in line
    for word in word_list:

        # applying lower() function to disable case-sensitivity when counting words
        word = word.lower()

        # if current word is an empty string, ignore it
        if word != '':

            # making entry for new word (adds one to value of word in dictionary if it already exists)
            word_dictionary[word] = word_dictionary.get(word, 0) + 1

# closing input file
input_file.close()

# opening file to write to
output_file = open(sys.argv[2], "w")

# sorting dictionary and formatting string to write to output file
for item in sorted(word_dictionary.items()):

    word = item[0]
    count = item[1]

    # writing to file
    output_file.write(word + " " + str(count) + "\n")

# closing output file
output_file.close()
