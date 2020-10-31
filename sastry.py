from tkinter import *
from tkinter import messagebox
root=Tk()
root.title('Tic-Tac-Toe')


#x person starts game so true
clicked= True
count= 0
#after winning disable buttons
def disable():
    A1.config(state=DISABLED)
    A2.config(state=DISABLED)
    A3.config(state=DISABLED)

    A4.config(state=DISABLED)
    A5.config(state=DISABLED)
    A6.config(state=DISABLED)

    A7.config(state=DISABLED)
    A8.config(state=DISABLED)
    A9.config(state=DISABLED)
#check to see if someone won
def check():
    global winner
    winner= False
#wins of player who chose x
    if A1["text"]=="x" and A2["text"]=="x" and A3["text"]=="x":
        A1.config(bg="green")
        A2.config(bg="green")
        A3.config(bg="green")
        messagebox.showinfo("winner","Player x wins")
        disable()
    elif A4["text"]=="x" and A5["text"]=="x" and A6["text"]=="x":
        A4.config(bg="green")
        A5.config(bg="green")
        A6.config(bg="green")
        messagebox.showinfo("winner","Player with x wins")
        disable()
    elif A7["text"]=="x" and A8["text"]=="x" and A9["text"]=="x":
        A7.config(bg="green")
        A8.config(bg="green")
        A9.config(bg="green")
        messagebox.showinfo("winner","Player with x wins")
        disable()
    elif A1["text"]=="x" and A4["text"]=="x" and A7["text"]=="x":
        A1.config(bg="green")
        A4.config(bg="green")
        A7.config(bg="green")
        messagebox.showinfo("winner","Player with x wins")
        disable()
    elif A2["text"]=="x" and A5["text"]=="x" and A8["text"]=="x":
        A2.config(bg="green")
        A5.config(bg="green")
        A8.config(bg="green")
        messagebox.showinfo("winner","Player with x wins")
        disable()
    elif A3["text"]=="x" and A6["text"]=="x" and A9["text"]=="x":
        A3.config(bg="green")
        A6.config(bg="green")
        A9.config(bg="green")
        messagebox.showinfo("winner","Player with x wins")
        disable()
    elif A1["text"]=="x" and A5["text"]=="x" and A9["text"]=="x":
        A1.config(bg="green")
        A5.config(bg="green")
        A9.config(bg="green")
        messagebox.showinfo("winner","Player with x wins")
        disable()
    elif A3["text"]=="x" and A5["text"]=="x" and A7["text"]=="x":
        A3.config(bg="green")
        A5.config(bg="green")
        A7.config(bg="green")
        messagebox.showinfo("winner","Player with x wins")
        disable()
#to check if player o wins
    elif A1["text"]=="o" and A2["text"]=="o" and A3["text"]=="o":
        A1.config(bg="green")
        A2.config(bg="green")
        A3.config(bg="green")
        messagebox.showinfo("winner","Player o wins")
        disable()
    elif A4["text"]=="o" and A5["text"]=="o" and A6["text"]=="o":
        A4.config(bg="green")
        A5.config(bg="green")
        A6.config(bg="green")
        messagebox.showinfo("winner","Player with o wins")
        disable()
    elif A7["text"]=="o" and A8["text"]=="o" and A9["text"]=="o":
        A7.config(bg="green")
        A8.config(bg="green")
        A9.config(bg="green")
        messagebox.showinfo("winner","Player with o wins")
        disable()
    elif A1["text"]=="o" and A4["text"]=="o" and A7["text"]=="o":
        A1.config(bg="green")
        A4.config(bg="green")
        A7.config(bg="green")
        messagebox.showinfo("winner","Player with o wins")
        disable()
    elif A2["text"]=="o" and A5["text"]=="o" and A8["text"]=="o":
        A2.config(bg="green")
        A5.config(bg="green")
        A8.config(bg="green")
        messagebox.showinfo("winner","Player with o wins")
        disable()
    elif A3["text"]=="o" and A6["text"]=="o" and A9["text"]=="o":
        A3.config(bg="green")
        A6.config(bg="green")
        A9.config(bg="green")
        messagebox.showinfo("winner","Player with o wins")
        disable()
    elif A1["text"]=="o" and A5["text"]=="o" and A9["text"]=="o":
        A1.config(bg="green")
        A5.config(bg="green")
        A9.config(bg="green")
        messagebox.showinfo("winner","Player with o wins")
        disable()
    elif A3["text"]=="o" and A5["text"]=="o" and A7["text"]=="o":
        A3.config(bg="green")
        A5.config(bg="green")
        A7.config(bg="green")
        messagebox.showinfo("winner","Player with o wins")
        disable()

    if count==9 and winner== False:
        messagebox.showinfo("Tic-Tac-Toe","It's a tie\n no one wins")
        disable()
        

#after clicking buttons
def A_click(a):
    global clicked, count
    if a["text"]==" " and clicked== True:
        a["text"]="x"
        clicked= False
        count +=1
        check()
    elif a["text"]==" " and clicked== False:
        a["text"]="o"
        clicked= True
        count+=1
        check()
    else:
        messagebox.showerror("Tic-Tac-Toe","That box has already been selected\nslelect another box")
        

    

def reset():
    winner=False
    global count
    count=0
    global clicked
    clicked=True
    global A1,A2,A3,A4,A5,A6,A7,A8,A9
    A1=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:A_click(A1))
    A2=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:A_click(A2))
    A3=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:A_click(A3))

    A4=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:A_click(A4))
    A5=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:A_click(A5))
    A6=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:A_click(A6))

    A7=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:A_click(A7))
    A8=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:A_click(A8))
    A9=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:A_click(A9))

    A1.grid(row=0,column=1)
    A2.grid(row=0,column=2)
    A3.grid(row=0,column=3)

    A4.grid(row=1,column=1)
    A5.grid(row=1,column=2)
    A6.grid(row=1,column=3)

    A7.grid(row=2,column=1)
    A8.grid(row=2,column=2)
    A9.grid(row=2,column=3)
   
#buttons of game
A1=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:A_click(A1))
A2=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:A_click(A2))
A3=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:A_click(A3))

A4=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:A_click(A4))
A5=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:A_click(A5))
A6=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:A_click(A6))

A7=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:A_click(A7))
A8=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:A_click(A8))
A9=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:A_click(A9))

A1.grid(row=0,column=1)
A2.grid(row=0,column=2)
A3.grid(row=0,column=3)

A4.grid(row=1,column=1)
A5.grid(row=1,column=2)
A6.grid(row=1,column=3)

A7.grid(row=2,column=1)
A8.grid(row=2,column=2)
A9.grid(row=2,column=3)

#creating options to reset  the game
my_menu=Menu(root)
root.config(menu=my_menu)

options_menu=Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="options",menu=options_menu)
options_menu.add_command(label="Reset Game",command=reset)

reset()
root,mainloop()
