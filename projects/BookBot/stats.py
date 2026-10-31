
def word_count(book: str) -> int:
    """
    Accepts a book as a string and returns its words count.

    Args:
        book(string): Book which has to be split and words to be counted.
    
    Returns:
        int: Returns the count of the words.
    """
    words_list = book.split()    
    return len(words_list)


def character_count(book: str) -> dict[str, int]:
    """
    Accepts a book as a string and returns its character count including whitespaces and special characters.

    Args:
        book(string): Book which has to be split into words and into characters to be counted.
    
    Returns:
        dict: Returns the count of the words as key, value pair. dict[str, int].
    """
    counts = {}
    for char in book:
        char = char.lower()
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

def sort_on(book_counts: tuple[str, int]) -> int:
    """
    Accepts tuple as input and returns the element from the 1st index position.

    Args:
        book_counts(tuple): Tuple which has char and count stored in it.
    
    Returns:
        int: Element present in the first position. 
    """
    return book_counts[1]

def chars_dict_to_sorted_list(book_dict: dict[str, int]) -> list[tuple[str, int]]:
    """
    Accepts dict as input and returns the list with tuple containing character and its count.

    Args:
        book_dict(dict): Dict which contains char as key and count of chars as value. 
    
    Returns:
        list[tuple[str, int]]: List of tuples containing dict (key, value) pairs. 
    """
    words_list = []
    for char, num in book_dict.items():
        words_list.append((char, num))
    words_list = sorted(words_list, reverse=True, key=sort_on)
    return words_list
