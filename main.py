def main():
    with open("books/frankenstein.txt") as file_object:
        contents = file_object.read()
        print(count_words(contents))
        print(count_letters(contents))


def count_words(text):
    return len(text.split())


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


if __name__ == "__main__":
    main()
