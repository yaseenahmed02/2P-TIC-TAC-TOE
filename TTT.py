from importlib.machinery import WindowsRegistryFinder
from tabnanny import check
from tkinter import *
from tkinter import messagebox
import time

from numpy import true_divide

root = Tk()
root.title("Tic Tac Toe")


background_image = PhotoImage(file="/bg3.gif")
background_label = Label(root, i = background_image)
background_label.place(x=0, y=0)



#X starts so true
clicked = True #if true, x's turn
count = 0

#button clicked function



def disable_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

def checkifwon():
    global winner
    winner = False
    if count == 9:
        messagebox.showinfo("Draw", "No Winner")
        time.wait(1000)
        reset()
    if (b1["text"] == b2["text"] and b2["text"] == b3["text"] and b3["text"] != " "):
        b1.config(highlightbackground="Red")
        b2.config(highlightbackground="Red")
        b3.config(highlightbackground="Red")
        winner = True
        mark_win = b1["text"]
        messagebox.showinfo("Tic Tac Toe", mark_win + " wins")
        disable_all_buttons()
    elif (b4["text"] == b5["text"] and b5["text"] == b6["text"] and b6["text"] != " "):
        b4.config(highlightbackground="Red")
        b5.config(highlightbackground="Red")
        b6.config(highlightbackground="Red")
        winner = True
        mark_win = b4["text"]
        messagebox.showinfo("Tic Tac Toe", mark_win + " wins")
        disable_all_buttons()
    elif (b7["text"] == b8["text"] and b8["text"] == b9["text"] and b9["text"] != " "):
        b7.config(highlightbackground="Red")
        b8.config(highlightbackground="Red")
        b9.config(highlightbackground="Red")
        winner = True
        mark_win = b7["text"]
        messagebox.showinfo("Tic Tac Toe", mark_win + " wins")
        disable_all_buttons()

    elif (b1["text"] == b4["text"] and b4["text"] == b7["text"] and b7["text"] != " "):
        b1.config(highlightbackground="Red")
        b4.config(highlightbackground="Red")
        b7.config(highlightbackground="Red")
        winner = True
        mark_win = b1["text"]
        messagebox.showinfo("Tic Tac Toe", mark_win + " wins")
        disable_all_buttons()
    elif (b2["text"] == b5["text"] and b5["text"] == b8["text"] and b8["text"] != " "):
        b2.config(highlightbackground="Red")
        b5.config(highlightbackground="Red")
        b8.config(highlightbackground="Red")
        winner = True
        mark_win = b2["text"]
        messagebox.showinfo("Tic Tac Toe", mark_win + " wins")
        disable_all_buttons()
    elif (b3["text"] == b6["text"] and b6["text"] == b9["text"] and b9["text"] != " "):
        b3.config(highlightbackground="Red")
        b6.config(highlightbackground="Red")
        b9.config(highlightbackground="Red")
        winner = True
        mark_win = b3["text"]
        messagebox.showinfo("Tic Tac Toe", mark_win + " wins")
        disable_all_buttons()
    elif (b1["text"] == b5["text"] and b5["text"] == b9["text"] and b9["text"] != " "):
        b1.config(highlightbackground="Red")
        b5.config(highlightbackground="Red")
        b9.config(highlightbackground="Red")
        winner = True
        mark_win = b1["text"]
        messagebox.showinfo("Tic Tac Toe", mark_win + " wins")
        disable_all_buttons()
    elif (b3["text"] == b5["text"] and b5["text"] == b7["text"] and b7["text"] != " "):
        b3.config(highlightbackground="Red")
        b5.config(highlightbackground="Red")
        b7.config(highlightbackground="Red")
        winner = True
        mark_win = b3["text"]
        messagebox.showinfo("Tic Tac Toe", mark_win + " wins")
        disable_all_buttons()
    


def b_click(b):
    global clicked, count
    if (b["text"] == " ") and clicked == True:
        b["text"] = "X"
        clicked = False
        count+=1
        checkifwon()
    elif (b["text"] == " ") and clicked == False:
        b["text"] = "O"
        clicked = True
        count+=1
        checkifwon()
    else:
        messagebox.showerror("Tic Tac Toe", "Box already selected\n Pick another box..")


def reset():
    #buttons
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global clicked, count
    clicked = True
    count = 0
    b1 = Button(root, text = " ", font=("Helvetica, 20"), height = 3, width=6, bg = "Silver", command=lambda:b_click(b1))
    b2 = Button(root, text = " ", font=("Helvetica, 20"), height = 3, width=6, bg = "Silver", command=lambda:b_click(b2))
    b3 = Button(root, text = " ", font=("Helvetica, 20"), height = 3, width=6, bg = "Silver", command=lambda:b_click(b3))

    b4 = Button(root, text = " ", font=("Helvetica, 20"), height = 3, width=6, bg = "Silver", command=lambda:b_click(b4))
    b5 = Button(root, text = " ", font=("Helvetica, 20"), height = 3, width=6, bg = "Silver", command=lambda:b_click(b5))
    b6 = Button(root, text = " ", font=("Helvetica, 20"), height = 3, width=6, bg = "Silver", command=lambda:b_click(b6))

    b7 = Button(root, text = " ", font=("Helvetica, 20"), height = 3, width=6, bg = "Silver", command=lambda:b_click(b7))
    b8 = Button(root, text = " ", font=("Helvetica, 20"), height = 3, width=6, bg = "Silver", command=lambda:b_click(b8))
    b9 = Button(root, text = " ", font=("Helvetica, 20"), height = 3, width=6, bg = "Silver", command=lambda:b_click(b9))


    #Grid
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)


my_menu = Menu(root)
root.config(menu=my_menu)
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu = options_menu)
options_menu.add_command(label="Reset Game", command = reset)

reset()

root.mainloop()