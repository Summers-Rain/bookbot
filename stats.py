def get_word_count(book_text):
    text = book_text
    word_count = len(text.split())
    return word_count

def get_character_count(book_text):
    text = book_text.lower()
    character_count = {}
    for char in text:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1

    return character_count

def sort_character_count(char_dict):
    chars_list = []

    for char, count in char_dict.items():
        char_info = {"char": char, "count": count}
        chars_list.append(char_info)

    def sort_on(dict):
        return dict["count"]

    chars_list.sort(reverse=True, key=sort_on)

    return chars_list

