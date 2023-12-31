/**
 * This program counts the number of vowels contained in the input string.
 *
 * It uses a regex approach by counting all the matches for each letter
 * in the vowel space.
 *
 * Assumptions:
 * ------------
 *  - all letters in input word are Unicode
 *  - no letters are punctuation marks (especially not "|")
 *  - vowels can be vowels from any language
 */

countWords = (inputWord, vowels = "aeiou") => {
  // then we create a regex string that will match any of the vowels
  // e.g. "(a|e|i|o|u)"
  inputWord = inputWord.toLowerCase();
  vowels = vowels.toLowerCase().split("");
  let regex_string = "(" + vowels.join("|") + ")";

  // then we match all occurrences and count the length of the matches
  let matches = [...inputWord.matchAll(regex_string)];
  let num_vowels = matches.length;

  console.log(`Vowel space: ${vowels}`);
  console.log(`Number of vowels in '${inputWord}': ${num_vowels}`);
};

// first, get the input word and vowel space from the terminal
let inputWord = process.argv[2];
let vowels = "aeiou";
if (process.argv.length == 4) {
  vowels = process.argv[3];
}
