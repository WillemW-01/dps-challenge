import sys

if len(sys.argv) < 2:
    exit("Usage: $ python vowel_counter.py <input_word>")

input_word = sys.argv[1]
vowels = "aeiou"
if len(sys.argv) == 3:
    vowels = sys.argv[2]

"""
Assumptions:
  - all letters are unicode
  - no letters are punctuation characters
  - letters can be any vowel or consonent in any language
"""

"""
method 1: simple counter loop using iterables
"""
num_vowels_1 = 0
for letter in input_word:
    if letter in vowels:
        num_vowels_1 += 1

"""
method 2: do the same as above, but more "pythonic"
"""
num_vowels_2 = 0
num_vowels_2 += sum([input_word.count(vowel) for vowel in vowels])

"""
method 3: use translation tables to convert all vowels to a letter that is
          not a consonent or vowel, and then count all of them
"""
translation_table = input_word.maketrans(vowels, "*" * len(vowels))
translated_word = input_word.translate(translation_table)
num_vowels_3 = translated_word.count("*")

all_equal = num_vowels_1 == num_vowels_2 == num_vowels_3
print(f"All methods got the same? {all_equal}")
if all_equal:
    print(f"Vowel space: {list(vowels)}")
    print(f"Number of vowels in '{input_word}': {num_vowels_1}")
else:
    print("Oops... let me try again")
