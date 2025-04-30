def count_words(book_text):
    split_text = book_text.split()
    words = len(split_text)
    return (f"{words} words found in the document")

def count_chars(book_text):
    lowercase_book_test = book_text.lower()
    letters = {}

    for letter in lowercase_book_test:
        if (letter in letters) == False:
            letters[letter] = 1
        else:
            letters[letter] +=1
    return letters

    #take book text as input
    #create dictionary with all letters set to 0
    #iterate through the book text
    #if letter is in dictionary, set value of it to +=1
    #get count of every word

