
/**
 * This class implements a simple vowel counter. That is, given an input word,
 * it will be able to count the amount of vowels present.
 * 
 * A custom vowel set can be used via arguments.
 * 
 * 
 * Usage:
 * ------
 * java VowelCounter <String inputWord> [String vowelSet]
 * 
 * Assumptions:
 * ------------
 * - all letters in input word are Unicode
 * 
 */

import java.util.Arrays;

public class VowelCounter {

  // the vowel space
  private char[] vowels;

  /**
   * Does the letter exist in the vowel space?
   * 
   * @param letter the character to check
   * @return true if letter is in vowel space, false if not
   */
  private boolean is_letter_vowel(char letter) {
    for (char c : this.vowels) {
      if (c == letter) {
        return true;
      }
    }
    return false;
  }

  /**
   * Constructor for creating a new vowel counter with a given vowel space
   * 
   * @param vowels the vowels to belong to this object
   */
  public VowelCounter(char[] vowels) {
    this.vowels = vowels;
  }

  /**
   * Returns the number of vowels from the vowel space that were found in the
   * input string
   * 
   * @param inputString the word to check
   * @return the integer number of vowels
   */
  public int count_vowels(String inputString) {
    int count = 0;
    for (char letter : inputString.toCharArray()) {
      if (this.is_letter_vowel(letter)) {
        count += 1;
      }
    }
    return count;
  }

  /**
   * Driver code to test the implementation
   * 
   * @param args
   */
  public static void main(String[] args) {
    String inputString = args[0];
    char[] vowels = { 'a', 'e', 'i', 'o', 'u' };
    if (args.length == 2) {
      vowels = args[1].toCharArray();
    }

    VowelCounter vowelCounter = new VowelCounter(vowels);
    int numVowels = vowelCounter.count_vowels(inputString);
    System.out.printf("Vowel space: %s\n", Arrays.toString(vowels));
    System.out.printf("Number of vowels in '%s': %d\n", inputString, numVowels);
  }
}
