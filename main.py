from stats import get_num_words
from stats import get_letter_counts
from stats import sort_letters

def get_book_text(path):
    file_contents = ""
    try:
        with open(path) as f:
            file_contents += f.read()
    except FileNotFoundError as e:
        print(e)
    return file_contents

def main():
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    book_file = sys.argv[1]
    frankenstein = get_book_text(book_file)
    word_count = get_num_words(frankenstein)
    letter_counts = get_letter_counts(frankenstein)
    sorted_letter_counts = sort_letters(letter_counts)
    print(f"Found {word_count} total words.")
    print("===============================\n letter counts\n===============================")
    for letter in sorted_letter_counts:
        print(f"{letter}: {letter_counts[letter]}")

main()