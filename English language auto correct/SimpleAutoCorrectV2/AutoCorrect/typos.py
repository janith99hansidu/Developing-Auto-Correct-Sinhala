# given a word make different collection of possible candidates
from itertools import chain

alphabet = "abcdefghijklmnopqrstuvwxyz"
"""
    ---sample usage---
    dict_of_words = {"mother"} # dictionary of english words
    word = Word("mothr")
    # Get all possible candidates
    # filter the candidates that are only in the english dictionary
    for word in list(word.candidates()):
        if word in dict_of_words:
            print(word)
"""


class Word:
    def __init__(self, word):
        self.word = word
        self.slices = tuple((word[:i], word[i:]) for i in range(len(word) + 1))

    def _delete(self):
        # generate words with one character delete
        for a, b in self.slices:
            if b:
                yield "".join((a, b[1:]))

    def _insert(self):
        # generate words with one character insert
        for a, b in self.slices:
            for letter in alphabet:
                yield "".join((a, letter, b))

    def _replace(self):
        # generate words with one character delete
        for a, b in self.slices:
            if b:
                for letter in alphabet:
                    yield "".join((a, letter, b[1:]))

    def _transpose(self):
        # generate words with two consecutive characters swapped
        for i in range(len(self.word) - 1):
            a = self.word[:i]
            b = self.word[i:i + 2]
            yield a + b[1] + b[0] + self.word[i + 2:]

    def candidates(self):
        # combines all the transformations to one iterable
        return chain(self._delete(), self._transpose(), self._replace(), self._insert())
