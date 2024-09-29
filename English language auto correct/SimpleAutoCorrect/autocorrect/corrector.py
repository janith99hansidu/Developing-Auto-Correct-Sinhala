# make a class to define and import to main.py
# edit_distance function to calculate edit distance
# pass dictionary of vocabulary of English text and calculate the edit distance

def edit_distance(word1, word2):

    # initialize variables to len word1 and word2
    m, n = len(word1), len(word2)
    # initialize the dp table
    # rows(m+1) are word1 # columns(n+1) are word2
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # initialize the first row and column with the same as column and row number
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(m + 1):
        dp[i][0] = i

    # calculater the minimum edit with tabulating the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # if the char values are matched copy from
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j] + 1,  # Delete
                               dp[i][j - 1] + 1,  # Insert
                               dp[i - 1][j - 1] + 2  # Replace
                               )

    return dp[m][n]


class AutoCorrector:
    def __init__(self, min_edit, dictionary):
        self.min_edit = min_edit
        self.dictionary = dictionary

    def correct_word(self, word):
        # initialize a list to store minimum edits matched words
        best_matches = []

        # iterate all the word in the dictionary and calculate the edit distance
        for dict_word in self.dictionary:
            # call the edit_distance and calculate the edit distance
            current_distance = edit_distance(word, dict_word)

            # if the current distance is smaller than edit distance
            if current_distance <= self.min_edit:
                best_matches.append(dict_word)

        return best_matches
