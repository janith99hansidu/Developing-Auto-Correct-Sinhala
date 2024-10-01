# make frequency dict in given text data
# if the frequency_dict.txt is available don't again create this frequency dict
#
import re
from collections import Counter


def load_corpus(file_path):
    word_counter = Counter()

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            """ in each line in the text corpus removes the leading numbers 
                and removes any number and make frequency dictionary """

            line = re.sub(r'^\d+\s+', '', line)
            # split the sentence in to words
            words = line.split()
            # clean the words remove any punctuations and non word charters
            cleaned_words = [re.sub(r'^[\W\d]+|[\W\d]+$', '', word) for word in words]
            # remove all the empty string from the word
            cleaned_words = [word.lower() for word in cleaned_words if word]
            # make the frequency dict
            word_freq = Counter(cleaned_words)



