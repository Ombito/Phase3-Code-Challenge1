# Data Structures and Algorithms

This repository contains Python code for three different functions:

- `is_balanced(expression)`: Determines whether an expression containing parentheses, curly braces, and square brackets is balanced.
- `remove_duplicates(sequence)`: Removes duplicates from a sequence (list or tuple) while maintaining the original order of elements.
- `word_frequency(sentence)`: Returns a dictionary containing the frequency of each word in a sentence, ignoring punctuation and considering words in a case-insensitive manner.
  
## Stacks 

### Question 1: is_balanced(expression)

An expression is considered balanced if each opening bracket has a corresponding closing bracket in the correct order.

Sample input:

    `expression1 = "([]{})"
    expression2 = "([)]"
    print(is_balanced(expression1))   Output: True
    print(is_balanced(expression2))   Output: False`

### Question 2: remove_duplicates(sequence)

This is a function that takes a list and returns a new sequence with duplicates removed while maintaining the original order of elements.

Sample input:

    `input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]`

Output:

    `[2, 3, 4, 5, 6, 7]`

### Question 3: word_frequency(sentence)

This is a function that takes a sentence and returns a dictionary containing the frequency of each word in the sentence. Ignore punctuation and consider words in a case-insensitive manner.

Sample input:

    `sentence = "This is a test sentence. This sentence is a test."
    result = word_frequency(sentence)
    print(result)`

Sample output:

    `{'this': 2, 'is': 2, 'a': 2, 'test': 2, 'sentence': 2}`


## Conclusion 

This README file provides a brief overview of my python assignment, the functions I have implemented, and how to use them.
