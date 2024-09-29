from autocorrect.corrector import AutoCorrector


def main():
    # read the dictionary words and make a dict
    # Define the path to the file
    file_path = "./data/dict.txt"
    dict_file = open(file_path, "r")

    # remove \n and store in the dict_word_list
    dict_word_list = [line.strip() for line in dict_file]

    # create an instance of AutoCorrector with the dictionary
    autocorrector = AutoCorrector(1, dict_word_list)

    # get the user input to incorrect word
    user_text = input("Enter text to correct: ")

    # call the correct_word method to give more suitable words
    suggested_words = autocorrector.correct_word(user_text)

    # print the suggested words
    print(f"Suggested words: {suggested_words}")

    dict_file.close()


if __name__ == "__main__":
    main()