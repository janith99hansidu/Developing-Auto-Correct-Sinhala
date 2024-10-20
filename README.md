# English Auto Correct

English Auto Correct is a simple spell-correction tool based on word frequency from a large text corpus. This project uses the Leipzig English dataset to clean, prepare, and process text for auto-correct suggestions.

## How It Works

The process involves:

1. **Data Cleaning**: Removing unwanted characters such as leading numbers and non-word characters.
2. **Corpus Preparation**: Building a frequency dictionary by counting word occurrences.
3. **Generating Edits**: Creating possible variations of the word (deletions, transpositions, replacements, insertions).
4. **Search for Correct Word**: Checking generated edits against the frequency dictionary.
5. **Providing Suggestions**: Suggesting the most likely correction based on word frequency.

## Example

Here’s a simple example of how the auto-correct functionality works:

```
Input: "appl"
Output: "apple"
```

## Sample Image

Here’s an illustration of how English Auto Correct works:

![English Auto Correct Sample Wrong Word](https://github.com/janith99hansidu/Developing-Auto-Correct-Sinhala/blob/main/src/sample_1.jpeg)
![English Auto Correct Sample Correct Word](https://github.com/janith99hansidu/Developing-Auto-Correct-Sinhala/blob/main/src/sample_2.jpeg)

---