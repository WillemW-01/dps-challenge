import os

COLOR_END = "\033[0m" # stops printing color
COLOR_PASSED = "\033[92m" # green color
COLOR_FAILED = "\033[91m" # red color
COMMANDS = {
    "python": "python vowel_counter.py",
    "java": "java VowelCounter.java",
    "js": "node vowelCounter.js",
}

def test_word(word, language, num_expected):
    """
    This function tests the specific implementation with an input word.
    
    It executes the appropriate command via a process, which will output the
    result to a file. The function then compares this result to the expected
    outcome.
    
    :param word: the word to count vowels from
    :param language: the string to determine which command to run
    :param num_expected: the number of vowels expected from the word
    :return None
    """
    print(f"Testing '{word}' in {language}: ", end="")


    try:
        os.system(f"{COMMANDS[language]} {word} > {language}_output.txt")
    except Exception as e:
        print("Something went wrong... ")
        exit(e)

    result = open(f"{language}_output.txt").read()
    index = result.rfind(":") + 1 # find the ": <num>"
    num_result = int(result[index:])
    if num_result == num_expected:
        print(f"{COLOR_PASSED}Passed!{COLOR_END}")
    else:
        print(f"{COLOR_FAILED}Failed{COLOR_END} (expected {num_expected}, got {num_result})")

if __name__ == "__main__":
  # fmt: off
  word_bank = {
      "We": 1, "are": 2, "very": 1, "happy": 1, "to": 1, "inform": 2, "you": 2,
      "that": 1, "we": 1, "decided": 3, "to": 1, "proceed": 3, "further": 2,
      "with": 1, "your": 2, "application": 5, "for": 1, "the": 1, "Software": 3,
      "Engineer": 4, "track": 1,
  } # fmt: on
  
  for language in ["python", "java", "js"]:
      for word in word_bank:
          test_word(word, language, word_bank[word])
