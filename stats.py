import sys

def get_book_text(path_to_file: str) -> str:
    with open(path_to_file, encoding="utf-8") as f:
        return f.read()

def count_words(text: str) -> int:
    words = text.split()
    return len(words)

def count_letters(text: str) -> dict:
    lower_text = text.lower()
    letter_counts = {}
    for char in lower_text:
        if char.isalpha():
            letter_counts[char] = letter_counts.get(char, 0) + 1
    return letter_counts

def sort_on(item):
    return item["num"]

def sorty_sorts(lst, sort):
    lst.sort(reverse=True, key=sort)  # in-place
    return lst

def pretty_print(sorted_list):
    for item in sorted_list:
        print(f"{item['char']}: {item['num']}")

def main():
    # Arg check
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]

    # Read once, reuse
    book_text = get_book_text(filepath)

    # Counts
    total_words = count_words(book_text)
    counts = count_letters(book_text)

    # Convert dict -> list[{'char': c, 'num': n}] and sort
    count_list = [{"char": c, "num": n} for c, n in counts.items()]
    sorted_list = sorty_sorts(count_list, sort_on)

    # Output
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    pretty_print(sorted_list)
    print("============= END ===============")

if __name__ == "__main__":
    main()
