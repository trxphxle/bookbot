import sys
from stats import get_num_words, count_characters, print_report

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    num_words = get_num_words(book_path)

    print_report(book_path)
    return num_words

main()