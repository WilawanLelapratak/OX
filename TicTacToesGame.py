from tkinter import *

import tkinter.messagebox
tk = Tk()
tk.title("OX")

click = True

def checker(buttons) :
    global click
    if buttons["text"] == " " and click == True :
        buttons["text"] = "X"
        click = False
    elif buttons["text"] == " " and click == False :
        buttons["text"] = "O"
        click = True

    elif(button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" and button4["text"] == "X" or
    button5["text"] == "X" and button6["text"] == "X" and button7["text"] == "X" and button8["text"] == "X" or
    button9["text"] == "X" and button10["text"] == "X" and button11["text"] == "X" and button12["text"] == "X" or
    button13["text"] == "X" and button14["text"] == "X" and button15["text"] == "X" and button16["text"] == "X" or
    button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" and button13["text"] == "X" or
    button2["text"] == "X" and button6["text"] == "X" and button10["text"] == "X" and button14["text"] == "X" or
    button3["text"] == "X" and button7["text"] == "X" and button11["text"] == "X" and button15["text"] == "X" or
    button4["text"] == "X" and button8["text"] == "X" and button12["text"] == "X" and button16["text"] == "X" or
    button1["text"] == "X" and button6["text"] == "X" and button11["text"] == "X" and button16["text"] == "X" or
    button4["text"] == "X" and button7["text"] == "X" and button10["text"] == "X" and button13["text"] == "X") :
        tkinter.messagebox.showinfo("Winner X", "You have just won a game!")

    elif(button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O" and button4["text"] == "O" or
    button5["text"] == "O" and button6["text"] == "O" and button7["text"] == "O" and button8["text"] == "O" or
    button9["text"] == "O" and button10["text"] == "O" and button11["text"] == "O" and button12["text"] == "O" or
    button13["text"] == "O" and button14["text"] == "O" and button15["text"] == "O" and button16["text"] == "O" or
    button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O" and button13["text"] == "O" or
    button2["text"] == "O" and button6["text"] == "O" and button10["text"] == "O" and button14["text"] == "O" or
    button3["text"] == "O" and button7["text"] == "O" and button11["text"] == "O" and button15["text"] == "O" or
    button4["text"] == "O" and button8["text"] == "O" and button12["text"] == "O" and button16["text"] == "O" or
    button1["text"] == "O" and button6["text"] == "O" and button11["text"] == "O" and button16["text"] == "O" or
    button4["text"] == "O" and button7["text"] == "O" and button10["text"] == "O" and button13["text"] == "O") :
        tkinter.messagebox.showinfo("Winner O", "You have just won a game!")

    else :
        tkinter.messagebox.showinfo("Game Tile!", "No Winner.")

buttons = StringVar()

button1 = Button(tk,text = " ", font = ('Times 25 bold'), height = 4, width = 8, command = lambda:checker(button1))
button1.grid(row = 1, column = 0, sticky = S+N+E+W)

button2 = Button(tk,text = " ", font = ('Times 25 bold'), height = 4, width = 8, command = lambda:checker(button2))
button2.grid(row = 1, column = 1, sticky = S+N+E+W)

button3 = Button(tk,text = " ", font = ('Times 25 bold'), height = 4, width = 8, command = lambda:checker(button3))
button3.grid(row = 1, column = 2, sticky = S+N+E+W)

button4 = Button(tk,text = " ", font = ('Times 25 bold'), height = 4, width = 8, command = lambda:checker(button4))
button4.grid(row = 1, column = 3, sticky = S+N+E+W)

button5 = Button(tk,text = " ", font = ('Times 25 bold'), height = 4, width = 8, command = lambda:checker(button5))
button5.grid(row = 2, column = 0, sticky = S+N+E+W)

button6 = Button(tk,text = " ", font = ('Times 25 bold'), height = 4, width = 8, command = lambda:checker(button6))
button6.grid(row = 2, column = 1, sticky = S+N+E+W)

button7 = Button(tk,text = " ", font = ('Times 25 bold'), height = 4, width = 8, command = lambda:checker(button7))
button7.grid(row = 2, column = 2, sticky = S+N+E+W)

button8 = Button(tk,text = " ", font = ('Times 25 bold'), height = 4, width = 8, command = lambda:checker(button8))
button8.grid(row = 2, column = 3, sticky = S+N+E+W)

button9 = Button(tk,text = " ", font = ('Times 25 bold'), height = 4, width = 8, command = lambda:checker(button9))
button9.grid(row = 3, column = 0, sticky = S+N+E+W)

button10 = Button(tk,text = " ", font = ('Times 25 bold'), height = 4, width = 8, command = lambda:checker(button10))
button10.grid(row = 3, column = 1, sticky = S+N+E+W)

button11 = Button(tk,text = " ", font = ('Times 25 bold'), height = 4, width = 8, command = lambda:checker(button11))
button11.grid(row = 3, column = 2, sticky = S+N+E+W)

button12 = Button(tk,text = " ", font = ('Times 25 bold'), height = 4, width = 8, command = lambda:checker(button12))
button12.grid(row = 3, column = 3, sticky = S+N+E+W)

button13 = Button(tk,text = " ", font = ('Times 25 bold'), height = 4, width = 8, command = lambda:checker(button13))
button13.grid(row = 4, column = 0, sticky = S+N+E+W)

button14 = Button(tk,text = " ", font = ('Times 25 bold'), height = 4, width = 8, command = lambda:checker(button14))
button14.grid(row = 4, column = 1, sticky = S+N+E+W)

button15 = Button(tk,text = " ", font = ('Times 25 bold'), height = 4, width = 8, command = lambda:checker(button15))
button15.grid(row = 4, column = 2, sticky = S+N+E+W)

button16 = Button(tk,text = " ", font = ('Times 25 bold'), height = 4, width = 8, command = lambda:checker(button16))
button16.grid(row = 4, column = 3, sticky = S+N+E+W)

tk.mainloop()
