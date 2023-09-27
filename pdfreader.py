import check
import choice
import keyboard
import methods
import os
from PyPDF2 import PdfReader


res_check = check.check_list()

tabs = res_check[1]

book = choice.book_choice(res_check[0])

reader = PdfReader(f"D:\PyProject\\reader_pdf\\books\\{book}")
   
num_page = res_check[1][book]


def render_text():
    global num_page
    os.system('cls')
    page = reader.pages[num_page]
    text = page.extract_text()
    print(text)


def right():
    global num_page
    num_page+=1
    tabs[book] = num_page
    render_text()
    methods.save(tabs)


def left():
    global num_page
    num_page-=1
    tabs[book] = num_page
    render_text()
    methods.save(tabs)


keyboard.add_hotkey("right", right)
keyboard.add_hotkey("left", left)


if __name__ == "__main__":
    render_text()


keyboard.wait('esc')

methods.save(tabs)
