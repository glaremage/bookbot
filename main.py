from stats import count_words, count_chars

def get_books(path):
    with open (path) as f:
        file_contents = f.read()
        return file_contents
    


def main():
    print(count_chars(get_books("./books/frankenstein.txt")))
main()