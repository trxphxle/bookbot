
def get_book_text(file_path):
    with open(file_path) as f:
        read_the_book = f.read()
    
    return read_the_book

def get_num_words(book_path):
    book_text = get_book_text(book_path)
    total_words = book_text.split()
    return len(total_words)

def count_characters(book_path):
    book_text = get_book_text(book_path)
    lowered_book_text = book_text.lower()
    
    all_characters = {}
    for ch in lowered_book_text:
        if ch in all_characters:
            all_characters[ch] += 1
        else: 
            all_characters[ch] = 1
    
    return all_characters

def sorted_dictionary(book_path):
    dictionary = count_characters(book_path)
    
    char_list = []
    for char, count in dictionary.items():
        char_list.append({"char": char, "num": count})
    
    char_list.sort(key=lambda x: x["num"], reverse=True)
    return char_list

def print_report(book_path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book_path)} total words")
    print("--------- Character Count -------")
    
    char_list = sorted_dictionary(book_path)
    for char_dict in char_list:
        print(f"{char_dict['char']}: {char_dict['num']}")
    
    print("============= END ==============")