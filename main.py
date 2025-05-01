import sys
from stats import count_words, count_chars, sort

def get_books(path):
    with open (path) as f:
        file_contents = f.read()
        return file_contents
    
    
    


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(get_books(sys.argv[1]))} total words")
    print("--------- Character Count -------")
    for items in sort(count_chars(get_books(sys.argv[1]))):
        if items["letter"].isalpha() == True:
            print(f"{items["letter"]}: {items["num"]}")
    print("============= END ===============")
main()