def main():
    with open("books/frankenstein.txt") as file_object:
        contents = file_object.read()
        print(count_words(contents))


def count_words(text):
    return len(text.split())


if __name__ == "__main__":
    main()
