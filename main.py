from stats import count_words, count_chars, sort

def get_books(path):
    with open (path) as f:
        file_contents = f.read()
        return file_contents
    


def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(get_books("./books/frankenstein.txt"))} total words")
    print("--------- Character Count -------")
    for items in sort(count_chars(get_books("./books/frankenstein.txt"))):
        if items["letter"].isalpha() == True:
            print(f"{items["letter"]}: {items["num"]}")
    print("============= END ===============")
main()