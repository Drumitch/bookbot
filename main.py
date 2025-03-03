def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

from stats import get_word_count
from stats import get_char_count
from stats import sort_counts

def main():
    book_path = "./books/frankenstein.txt"
    book = get_book_text(book_path)
    word_count = get_word_count(book)
    character_counts = get_char_count(book)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    sorted_counts = sort_counts(character_counts)
    for item in sorted_counts:
        print(f"{item['char']}: {item['count']}")
    
    print("============= END ===============")

    
if __name__ == "__main__":
    main()