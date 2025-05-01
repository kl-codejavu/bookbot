from stats import (
    get_num_words,
    get_char_frequency,
    char_frequency_to_sorted_list
)

import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit([1])
    book_path = sys.argv[1]
    file_contents = get_book_text(book_path)
    num_words = get_num_words(file_contents)
    char_frequency = get_char_frequency(file_contents.lower())
    char_frequency_sorted = char_frequency_to_sorted_list(char_frequency)
    print_report(book_path, num_words, char_frequency_sorted)

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def print_report(book_path, num_words, frequency_sorted):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in frequency_sorted:
        if not item["char"].isalpha():
                continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()
