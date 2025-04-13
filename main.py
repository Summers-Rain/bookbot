import sys
from stats import get_word_count
from stats import get_character_count
from stats import sort_character_count

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    with open(book_path) as f:
        book_text = f.read()
        
    word_count = get_word_count(book_text)
    character_count = get_character_count(book_text)
    sort_list = sort_character_count(character_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for char_dict in sort_list:
        char = char_dict["char"]
        if char.isalpha():
            count = char_dict["count"]
            print(f"{char}: {count}")

    print("============= END ===============")

main()