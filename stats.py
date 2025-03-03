def get_word_count(book):
    from main import get_book_text
    words = get_book_text("./books/frankenstein.txt").split()
    num_words = len(words)
    return num_words 

def get_char_count(text):
    text = text.lower()
    counts = {}
    for char in text:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts 

def sort_counts(char_dict):
    def sort_on(dict):
        return dict["count"]
    chars_list = []
    for key, value in char_dict.items():
        if key.isalpha():
            chars_list.append({"char": key, "count": value})
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list
