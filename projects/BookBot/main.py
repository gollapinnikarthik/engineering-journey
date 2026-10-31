import sys
from stats import word_count, character_count, chars_dict_to_sorted_list

def get_book_text(file_path: str) -> str:
    """
    Accepts a file path as a string and reads the file contents.

    Args:
        file_path(string): File Path which has to be opened to be read.
    
    Returns:
        str: Returns the file's contents as a string.
    """

    with open(file_path) as file:
        return file.read()

def print_report(file_path: str, word_count: int, sorted_character_list: list) -> None:
    """
    Accepts file path, words count and sorted words list and prints in a proper word fromat

    Agrs:
        file_path(string): File Path which has to be opened to be read.
        word_count(int): Total words count in the file.
        sorted_character_list(list): List of characters along with the counts as tuples in a list.
    Returns:
        None
    """
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print('----------- Word Count ----------')
    print(f"Found {word_count} total words")
    print('--------- Character Count -------')
    for char, num in sorted_character_list:
        if not char.isalpha():
            continue
        print(f"{char}: {num}")
    print('============= END ===============')


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    #print(get_book_text(file_path))
    count = word_count(book_text)
    #print(f"Found {count} total words")
    characters_count = character_count(book_text)
    #print(characters_count)
    sorted_words_list = chars_dict_to_sorted_list(characters_count)
    #print(sorted_words_list)
    print_report(file_path, count, sorted_words_list)


if __name__ == "__main__":
    main()