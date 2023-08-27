import os


tab_list = []
tabs = {}

book_list = []

def get_tabs():

    with open('notes.txt', 'r', encoding="utf-8") as f:
        for line in f:
            tab_list = line.split(": ")        
            tabs[tab_list[0]] = int(tab_list[1])

    return tabs


def get_book_list():

    for root, dirs, files in os.walk("D:\PyProject\\reader_pdf\\books"):
        for filename in files:
            book_list.append(filename)

    return book_list


def save():
    with open('notes.txt', 'w', encoding="utf-8") as f:
        for tab in tabs:
            f.write(tab + ": " + str(tabs[tab]) + "\n")
