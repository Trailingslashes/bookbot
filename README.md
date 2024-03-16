# Book Bot

This project is a code assistant that was trained by Tabnine. It can be used to analyze text files and generate reports based on the contents of the files.

## Project Structure

This project has a main.py file in the root directory, and a books directory that contains a text file called frankenstein.txt.

## How to Use

To use this project, you can run the main.py file. This will prompt you to enter the path to the text file you want to analyze. Once you enter the path, the program will read the contents of the file and generate a report.

## Code Snippets

Here are some code snippets from the main.py file:

```
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
```

This code defines functions for counting words, counting letters, creating a report, and reading the contents of a file. The main function takes the path to the frankenstein.txt file as input, reads the contents of the file, and then calls the other functions to generate the report.
