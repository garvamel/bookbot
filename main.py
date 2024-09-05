def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print_report(text, book_path)


def print_report(text, path):
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    print(f"---- Begin of report for {path} ----")
    print(f"{num_words} words found in the document\n")
    for char in num_chars:
        print(f"The '{char}' character was found {num_chars[char]} times")
    print(f"\n---- End of report ----")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_chars(text):
    l_text = text.lower()
    alphabet =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    char_count = dict.fromkeys(alphabet,0) 
    for char in l_text:
        if char in alphabet:
            char_count[char] += 1
    return char_count

main()
