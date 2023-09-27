import os
import json


tabs = {}

book_list = []

def get_tabs():

    with open('D:/PyProject/reader_pdf/notes.json', 'r', encoding="utf-8") as f:
        tabs = json.load(f)

    return tabs


def get_book_list():

    for root, dirs, files in os.walk("D:\PyProject\\reader_pdf\\books"):
        for filename in files:
            book_list.append(filename)

    return book_list


def save(tabs):
    with open('D:/PyProject/reader_pdf/notes.json', 'w', encoding="utf-8") as f:
        json.dump(tabs, f, indent=2, ensure_ascii=False)

