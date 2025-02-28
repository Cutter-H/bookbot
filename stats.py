def get_num_words(book_string):
    words = book_string.split()
    return len(words)

def get_letter_counts(book_string):
    letter_counts = {}
    for C in book_string:
        c = C.lower()
        if c in letter_counts:
            letter_counts[c] += 1
        else:
            letter_counts[c] = 1
    return letter_counts

def sort_letters(letters_dict):
    sorted = []
    for letter in letters_dict:
        if letter.isalpha():
            sorted.append(letter) 
    sorted.sort()
    return sorted
    sorted_dict = {}
    for letter in sorted:
        sorted_dict[letter] = letters_dict
    return sorted_dict