import sys

# This function takes a file path as input and returns the contents of the file as a text string
def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

from stats import get_word_count
from stats import get_char_count
from stats import sort_counts

# This function prints a report containing the word and alphabetic character counts
# of a file converted to text with the get_book_path function
def main():
    try:
        
        if len(sys.argv) > 1 or len(sys.argv) < 1:
            book_path = sys.argv[1]
            print(book_path)
        else:
            print("You must provide exactly two arguments.")

        book = get_book_text(book_path)
        word_count = get_word_count(book)
        character_counts = get_char_count(book)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")

        sorted_counts = sort_counts(character_counts)
        for item in sorted_counts:
            print(f"{item['char']}: {item['count']}")
        
        print("============= END ===============")
                    
    except Exception as e:
        print(f"Error. {e}.")

# This if statement is included to prevent circular importing between stats.py and main.py
if __name__ == "__main__":
    main()