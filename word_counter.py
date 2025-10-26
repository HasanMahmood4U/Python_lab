import string

def count_word_occurrences(text):
    """
    Counts the occurrence of each word in a given string after cleaning it.

    Args:
        text (str): The input string to analyze.

    Returns:
        dict: A dictionary where keys are the words and values are their counts.
    """

    # 1. Convert the entire string to lowercase to treat "The" and "the" as the same word
    text = text.lower()

    # 2. Remove punctuation from the string
    # This is important so "apple." and "apple" are counted as the same word
    # We use a translation table to replace all punctuation characters with a space
    translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
    text_without_punc = text.translate(translator)

    # 3. Split the cleaned string into a list of words
    # split() handles multiple spaces created by the punctuation removal gracefully
    words = text_without_punc.split()

    # 4. Use a dictionary to store the word counts
    word_counts = {}

    # 5. Iterate through the words and count them
    for word in words:
        # Skip empty strings that might result from extra spaces
        if word:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1

    return word_counts

input_string = (
    "The quick brown fox jumps over the lazy dog. "
    "The fox is quick, but the dog is very lazy."
)

print(f"Original String:\n'{input_string}'\n")

# Get the results
results = count_word_occurrences(input_string)

print("Word Occurrences:")
# Iterate through the dictionary and print the results clearly
for word, count in sorted(results.items()):
    print(f"'{word}': {count}")

# Bonus: Using the built-in 'collections.Counter' for a faster, more Pythonic solution
from collections import Counter

def count_word_occurrences_pythonic(text):
    # Same cleaning steps
    text = text.lower()
    translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
    text_without_punc = text.translate(translator)
    words = text_without_punc.split()
    return Counter(words)

print("\n--- Pythonic Solution using collections.Counter ---")
pythonic_results = count_word_occurrences_pythonic(input_string)
print(pythonic_results)