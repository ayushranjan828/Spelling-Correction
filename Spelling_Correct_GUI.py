from tkinter import *
from textblob import TextBlob

def correct_spell():
    get_data = enter1.get()
    corr = TextBlob(get_data)
    data = corr.correct()

    # Delete data which is present in Enter2 column and rewrite new generated data
    enter2.delete(0, END)
    enter2.insert(0,data)

def main_window():

    # Declaring global variable so we can easily access it in another function
    global enter1, enter2

    win = Tk()

    win.geometry("500x400")
    win.resizable(False, False)
    win.config(bg = "Blue")
    win.title("Spelling Checker")

    lable1 = Label(win, text = "Incorrect Spelling", font = ("Time New Roman", 25, "bold"), bg = "Blue", fg = "white")
    lable1.place(x = 100, y = 20, height = 50, width = 300)

    enter1 = Entry(win, font = ("Time New Roman", 22), bg = "ghost white")
    enter1.place(x = 50, y = 80, height = 50, width = 400)

    lable2 = Label(win, text = "Correct Spelling", font = ("Time New Roman", 25, "bold"), bg = "Blue", fg = "white")
    lable2.place(x = 100, y = 140, height = 50, width = 300)

    enter2 = Entry(win, font = ("Time New Roman", 22), bg = "ghost white")
    enter2.place(x = 50, y = 200, height = 50, width = 400)


    # comand = correct_spell is function of spelling correction
    button = Button(win, text = "Done", font = ("Time New Roman", 22, "bold"), bg = "Red", command = correct_spell)
    button.place(x = 200, y = 260, height = 50, width = 100)

    win.mainloop()

main_window()