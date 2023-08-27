import methods


def check_list():
    
    res = []

    tabs = methods.get_tabs()
    book_list = methods.get_book_list()
    book_del = []


    for book in book_list:
        if book not in tabs:
            tabs[book] = 0
    

    for elem in tabs:
        if elem not in book_list:
            book_del.append(elem)


    for elem in book_del:
        tabs.pop(elem, None)


    methods.save()

    res = [book_list, tabs]

    return res
