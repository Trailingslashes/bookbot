def main():
    book_path = "books/frankenstein.txt"
    contents = read_contents(book_path)
    print("--- Begin report of books/frankenstein.txt ---")
    count_words(contents)
    # print a new line
    print()
    create_report(contents)


def count_words(text):
    counted_words = len(text.split())
    print(f"{counted_words} words found in the document")


def count_letters(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    text = text.lower()
    letter_count = {}

    # Count occurrences of each letter in the text
    for letter in text:
        if letter in alphabet:
            letter_count[letter] = letter_count.get(letter, 0) + 1

    # Sort the dictionary by keys (letters) and return a new dictionary
    sorted_dictionary = {letter: letter_count[letter]
                         for letter in sorted(letter_count)}

    return sorted_dictionary


def create_report(dictionary):
    sorted_dictionary = count_letters(dictionary)
    for k, v in sorted_dictionary.items():
        print(f"The '{k}' character was found {v} times")


def read_contents(path):
    with open(path) as f:
        path = f.read()
    return path


if __name__ == "__main__":
    main()
