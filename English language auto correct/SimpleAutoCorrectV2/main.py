# create frequency dictionary from text corpus
# when a word typed if the word in the dict nothing to do
# otherwise generate the possible candidates of given word
# filter the candidates that are in the dict
# show most probable answer with the help of the frequency dict
from AutoCorrect.frequency import load_freq_dict_from_file
from AutoCorrect.typos import Word


class Speller:
    def __init__(self, threshold):
        self.frequency_dict = load_freq_dict_from_file("./data/output.json", "./data/eng_news_2005_10K-sentences.txt")
        self.threshold = threshold  # return only most probable candidates

    def get_candidates(self, word):
        # if the word already in the frequency dict.keys() that means it is correct word no candidates
        # otherwise check for candidates
        if word in self.frequency_dict:
            return []

        return sorted([(candidate, self.frequency_dict[candidate])
                       for candidate in Word(word).candidates()
                       if candidate in self.frequency_dict],
                      key=lambda x: x[1],
                      reverse=True)[:self.threshold]


if __name__ == '__main__':
    # set the threshold value to how many of most probable words that should return
    threshold_value = 3
    # create speller object to get candidates
    speller = Speller(threshold_value)
    print('input a word: ')
    word = input().lower()
    print("possible corrections :", speller.get_candidates(word))
