def book_choice(book_list):

    cur_book = ""

    print(f"Выберите книну из списка: (1-{len(book_list)})")

    for i in range(0, len(book_list)):
        print(f"{i + 1}) {book_list[i]}")

    cur_book = int(input())

    cur_book_name = book_list[(cur_book)-1]

    return cur_book_name