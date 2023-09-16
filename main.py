#function is_balanced

#function remove_duplicates
#takes in a list urgument
#return no duplicates from the list 

def remove_duplicates(list):
    list = [2, 3, 2, 4, 5, 3, 6, 7, 5]
    new_list = set(list)
    print(new_list)
remove_duplicates(list)

#function word_frequency
#parameter is a sentence
#returns a dictionary containing a word frequency