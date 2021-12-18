import random
from tkinter import *

window = Tk()
window.geometry("500x260")

window.title("Password Generation")
found = 0


def get_passwd():
    global found
    alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    symbols = "_:;><.,!@#$%^&*?/\|"
    number = "1234567890"

    alpha_lst = list(alphabets)
    sym_lst = list(symbols)
    num_lst = list(number)

    passwd_lst = []
    char = ""

    for characters in range(0, 50):
        num1 = random.randint(0, len(alpha_lst) - 1)
        num2 = random.randint(0, len(sym_lst) - 1)
        num3 = random.randint(0, len(num_lst) - 1)
        passwd_lst.append(alpha_lst[num1])
        passwd_lst.append(sym_lst[num2])
        passwd_lst.append(num_lst[num3])

    random.shuffle(passwd_lst)
    passwd_lst = passwd_lst[0: Scroll1.get() + 1]

    for values in range(0, len(passwd_lst) - 1):
        char = char + passwd_lst[values]

    passwd_lst.clear()
    if found == 0:
        text.insert(END, char)
        found = 1


def clear():
    global found
    text.delete("1.0", END)
    found = 0


# Creating a line
canvas = Canvas(window)
Line = canvas.create_line(290, 30, 290, 240)
canvas.pack(fill=BOTH, expand=True)

# Adding text
text = Text(window, font=("TimesNewRoman", 15), height=7, width=15, bd=3)
text.place(x=300, y=70)

text1 = Text(window, font=("TimesNewRoman", 15), height=1, width=24, bd=3)
text1.place(x=10, y=30)
text1.insert(END, "Number of digits in password: ")

text2 = Text(window, font=("TimesNewRoman", 15), height=1, width=15, bd=3)
text2.place(x=300, y=30)
text2.insert(END, "Password: ")

# Making a Scale(6-50)
Scroll1 = Scale(window, from_=6, to=50, length=200, tickinterval=5, orient=HORIZONTAL)
Scroll1.place(x=50, y=75)

# Making Buttons to
Button1 = Button(window, text="Generate", font=("TimesNewRoman", 15), height=1, width=24, command=get_passwd)
Button1.place(x=10, y=150)

Button2 = Button(window, text="Clear", font=("TimesNewRoman", 15), height=1, width=24, command=clear)
Button2.place(x=10, y=200)

window.resizable(False, False)
window.mainloop()
