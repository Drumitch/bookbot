import sys
# This funnction reads a text file and outputs the number of words that appear within it.
def get_word_count(book):
    from main import get_book_text
    book_path = sys.argv[1]
    words = get_book_text(book_path).split()
    num_words = len(words)
    return num_words 

# This function takes a text file as input and outputs a dictionary that tracks the number 
# of instances of each character that appears within.
def get_char_count(text):
    text = text.lower()
    counts = {}
    for char in text:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts 

# This function takes a dictionary as input and sorts the dictionary by frequency of appearance
# of each alphabetic character that appears within.
def sort_counts(char_dict):
    def sort_on(dict):
        return dict["count"]
    chars_list = []
    for key, value in char_dict.items():
        if key.isalpha():
            chars_list.append({"char": key, "count": value})
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list
