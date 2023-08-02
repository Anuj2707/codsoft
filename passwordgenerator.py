from tkinter import *
import string
import random
import pyperclip
import tkinter

def gen():
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    numbers = string.digits
    special = string.punctuation

    mix = lower + upper + numbers + special
    passwordlength = int(length1.get())

    password = ""

    if choose.get() == 1:
        passwords = ''.join(random.choices(lower, k=passwordlength))

    elif choose.get() == 2:
        passwords = ''.join(random.choices(lower + upper + numbers, k=passwordlength))

    elif choose.get() == 3:
        passwords = ''.join(random.choices(mix, k=passwordlength))

    passfield.delete(0, 'end')
    passfield.insert(0, passwords)

def copy():
    random_password = passfield.get()
    pyperclip.copy(random_password)

win = tkinter.Tk()
win.title("Random Password Generator")
win.geometry("600x580")
win.resizable(False, False)
win.config(bg='white')
choose = IntVar()
Font = ('poppins', 18, 'bold')
passwordLabel = Label(win, text='Password Generator', font=('times new roman', 20, 'bold'), bg='black', fg='white')
passwordLabel.grid(pady=10)

# images
t_img = PhotoImage(file="titimg.png")
win.iconphoto(False, t_img)

# radio
weak = Radiobutton(win, text='Poor', value=1, variable=choose, font=Font)
weak.place(x=40, y=100)

medium = Radiobutton(win, text='Average', value=2, variable=choose, font=Font)
medium.place(x=200, y=100)

strong = Radiobutton(win, text='Strong', value=3, variable=choose, font=Font)
strong.place(x=390, y=100)

# label
lengthpassword = Label(win, text='Password Length', font=Font, bg='black', fg='white')
lengthpassword.place(x=190, y=190)

# spinbox
length1 = Spinbox(win, from_=8, to_=25, width=7, font=Font)
length1.place(x=230, y=240)

# button
b1 = Button(win, text='Generate', font=Font, command=gen, fg="white", bg="red")
b1.place(x=190, y=300)

# entry
passfield = Entry(win, width=25, bd=2, font=Font,fg="red")
passfield.place(x=100, y=365)

# button copy
b2 = Button(win, text='Copy', font=Font, command=copy, fg="white", bg="blue")
b2.place(x=218, y=430)

win.mainloop()
