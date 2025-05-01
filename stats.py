def count_words(book_text):
    split_text = book_text.split()
    words = len(split_text)
    return (words)

def count_chars(book_text):
    lowercase_book_test = book_text.lower()
    letters = {}

    for letter in lowercase_book_test:
        if (letter in letters) == False:
            letters[letter] = 1
        else:
            letters[letter] +=1
    return letters

def sort_on(dict):
    return dict["num"]

def sort(dict_letters):
    unsorted_list = []
    empty_dict = {}
    for key in dict_letters:
        keyval = dict_letters[key]
        unsorted_list.append({"letter": key,"num": keyval})
    
    unsorted_list.sort(reverse=True, key=sort_on)
    return unsorted_list

