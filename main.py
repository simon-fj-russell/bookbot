def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print_report(count_characters(text))


def get_book_text(path):
    with open(path) as f:
        return f.read()
    

def count_characters(text):
    text = text.lower()
    character_dict = {}
    for char in text:
        if char in character_dict:
            character_dict[char] += 1
        else:
            character_dict[char] = 1

    return character_dict


def sort_on(dict):
    return dict["count"]


def print_report(text):
    letters = []
    for key, value in text.items():
        if key.isalpha():
            letters.append({"name": key, "count": value})

    letters.sort(reverse=True, key=sort_on)

    print("--- Begin report of books/frankenstein.txt ---")
    print("77986 words found in the document")
    for x in letters:
        print(f"The character '{x['name']}' was found {x['count']} times")
    print("--- End report ---")

main()