# make frequency dict in given text data
# if the frequency_dict.txt is available don't again create this frequency dict
import json
import os
import re
from collections import Counter, OrderedDict

"""
---sample usage---

# where the text corpus is located
text_corpus_file_path = "../data/eng_news_2005_10K-sentences.txt"

# where the frequency dictionary file is located
frequency_dict_file_path = "../data/output.json"

# load frequency dict from file or create a new one if not found
frequency_dict = load_freq_dict_from_file(frequency_dict_file_path, text_corpus_file_path)
"""


def load_corpus(corpus_file_path):
    """ in each line in the text corpus removes the leading numbers
                    and removes any number and make frequency dictionary """
    word_counter = Counter()

    with open(corpus_file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # split the sentence into words
            words = line.split()
            # clean the words remove any punctuations and non-word characters
            cleaned_words = [re.sub(r'^[\W\d]+|[\W\d]+$', '', word) for word in words]
            # remove all the empty string from the word
            cleaned_words = [word.lower() for word in cleaned_words if word]
            # add the words to dict
            word_counter.update(cleaned_words)

    return dict(word_counter)


def load_freq_dict_from_file(freq_dict_file_path, text_corpus_file_path):
    """if output file exists in the directory load frequency dict from it
        else build the frequency dict"""
    if os.path.exists(freq_dict_file_path):
        with open(freq_dict_file_path, 'r', encoding='utf-8') as f:
            # convert loaded dict values back to int
            frequency_dict = {word: int(count) for word, count in json.load(f).items()}
        return frequency_dict
    else:
        # if the frequency_dict_file is not in the path make a dict
        frequency_dict = load_corpus(text_corpus_file_path)
        # sort the frequency dictionary
        ordered_frequency_dict = OrderedDict(sorted(frequency_dict.items(), key=lambda x: x[1], reverse=True))
        # and save the corpus into the output.json
        with open(freq_dict_file_path, 'w', encoding='utf-8') as f:
            json.dump(ordered_frequency_dict, f, ensure_ascii=False)

        return frequency_dict
