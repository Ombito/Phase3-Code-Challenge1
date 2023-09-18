import string

def is_balanced(expression):
    sample = []  

    for item in expression:
        if item in '([{':
            sample.append(item)
        elif item in ')]}':
            if not sample:
                return False
            new = sample.pop()
            if (new == '(' and item != ')') or (new == '[' and item != ']') or (new == '{' and item != '}'):
                return False

    return not sample
expression = "([], [)"
print(is_balanced(expression))


def remove_duplicates(list):
    list = [2, 3, 2, 4, 5, 3, 6, 7, 5]
    new_list = set(list)
    print(new_list)
remove_duplicates(list)


def word_frequency(sentence):
    sentence = sentence.translate(str.maketrans('', '', string.punctuation)).lower()
    letters = sentence.split()

    sentence_dict = {}
    
    for letter in letters:
        if letter in sentence_dict:
            sentence_dict[letter] += 1
        else:
            sentence_dict[letter] = 1
    
    return sentence_dict
sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)

