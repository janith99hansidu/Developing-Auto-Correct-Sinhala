# make frequency dict in given text data
# if the frequency_dict.txt is available don't again create this frequency dict
import json
import os
import re
from collections import Counter


def load_corpus(corpus_file_path):
    """ in each line in the text corpus removes the leading numbers
                    and removes any number and make frequency dictionary """
    word_counter = Counter()

    with open(corpus_file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # split the sentence in to words
            words = line.split()
            # clean the words remove any punctuations and non word charters
            cleaned_words = [re.sub(r'^[\W\d]+|[\W\d]+$', '', word) for word in words]
            # remove all the empty string from the word
            cleaned_words = [word.lower() for word in cleaned_words if word]
            # add the words to dict
            word_counter.update(cleaned_words)

        return dict(word_counter)


class FrequencyDict:
    def __init__(self, freq_dict_file_path, text_corpus_file_path):
        self.freq_dict_file_path = freq_dict_file_path
        self.text_corpus_file_path = text_corpus_file_path

    def load_freq_dict_from_file(self):
        """if output file is exist in the directory load frequency dict from it
            else build the frequency dict"""
        if os.path.exists(self.freq_dict_file_path):
            with open(self.freq_dict_file_path, 'r', encoding='utf-8') as f:
                # convert loaded dict values back to int
                frequency_dict = {word: int(count) for word, count in json.load(f).items()}

            return frequency_dict
        else:
            # if the frequency_dict_file is not in the path make a dict
            frequency_dict = load_corpus(self.text_corpus_file_path)
            # and save the corpus in to the output.json
            with open(self.freq_dict_file_path, 'w', encoding='utf-8') as f:
                json.dump(frequency_dict, f)

            return frequency_dict

    """ ---sample usage---
    
    # where the text corpus is located
    text_corpus_file_path = "../data/eng_news_2005_10K-sentences.txt"
    
    # where the frequency dictionary file is located 
    frequency_dict_file_path = "../data/output.json"
    
    # make an object from frequency dict class
    frequency_dict_obj = FrequencyDict(frequency_dict_file_path, text_corpus_file_path)
    
    # call the method load_freq_dict_from_file()
    # returns a dictionary of frequencies of text corpus
    frequency_dict_obj.load_freq_dict_from_file()
    
    """
