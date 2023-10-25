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
 */

// first, get the input word and vowel space from the terminal
let inputWord = process.argv[2].toLowerCase();
let vowels = "aeiou".split("");
if (process.argv.length == 4) {
  vowels = process.argv[3].toLowerCase().split("");
}

// then we create a regex string that will match any of the vowels
// e.g. "(a|e|i|o|u)"
let regex_string = vowels.join("|");

// then we match all occurrences and count the length of the matches
let matches = [...inputWord.matchAll(`(${regex_string})`)];
let num_vowels = matches.length;

console.log(`Vowel space: ${vowels}`);
console.log(`Number of vowels in '${inputWord}': ${num_vowels}`);
