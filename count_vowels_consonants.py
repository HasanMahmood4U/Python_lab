# Program: Count vowels and consonants in a string
# -----------------------------------------------
# This script reads a line of text from the user, then counts how many
# alphabetic characters are vowels and how many are consonants.
#
# Notes:
# - We treat only letters (A-Z/a-z). Non-letters (digits, spaces, punctuation)
#   are ignored for the counts.
# - The letter 'y' is considered a consonant in this simple approach.

# Read a string from the user (keeps spaces and punctuation as entered)
text = input("Enter a string: ")

# Define the set of vowels for quick membership checks (lowercase for simplicity2
vowels_set = set("aeiou")

# Initialize counters
vowel_count = 0
consonant_count = 0

# Iterate over each character in lowercase form
for ch in text.lower():
    if ch.isalpha():               # Count only alphabetic characters
        if ch in vowels_set:       # If it's a vowel
            vowel_count += 1
        else:                      # Otherwise, it's a consonant
            consonant_count += 1

# Display the results
print("Vowels:", vowel_count)
print("Consonants:", consonant_count)

