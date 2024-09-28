# make a class to define and import to main.py
# edit_distance function to calculate edit distance
# pass dictionary of vocabulary of English text and calculate the edit distance

class AutoCorrector:
    def __init__(self, min_edit, dictionary):
        self.min_edit = min_edit
        self.dictionary = dictionary

    def