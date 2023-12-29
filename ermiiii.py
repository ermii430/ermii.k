from textblob import TextBlob
import tkinter
from tkinter import *
from tkinter import messagebox

def Correct_spelling():
    get_data = enter1.get()
    corr = TextBlob(get_data)
    data = corr.correct()
    enter2.delete(0,END)
    enter2.insert(0,data)



def main_window():
    global enter1,enter2
    win = Tk()
    win.geometry("500x370")
    win.resizable(False,False)
    win.config(bg="green")
    win.title("Wscube Tech")

    label1 = Label(win,text="Incorrect Spelling",font=("Time New Roman",25,"bold"),bg = "black",fg = "white")
    label1.place(x=100,y=20,height=50,width=300)

    enter1 = Entry(win,font=("Time New Roman",20))
    enter1.place(x=50,y = 80 ,height=50,width=400)

    label2 = Label(win,text="Correct Spelling",font=("Time New Roman",25,"bold"),bg = "black",fg = "white")
    label2.place(x=100,y=140,height=50,width=300)

    enter2 = Entry(win,font=("Time New Roman",20))
    enter2.place(x=50,y = 200 ,height=50,width=400)

    button = Button(win,text="check",font=("Time New Roman",25,"bold"),bg="yellow",command=Correct_spelling)
    button.place(x = 150, y = 280,height=50,width=200)
    win.mainloop()
def signin():
    username=user.get()
    password=code.get()

    if username=='admin' and password=='1234':
        root.destroy()
        main_window()

root=Tk()
root.title('login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)


        

img = PhotoImage(file='login.png')
Label(root,image=img,bg='white').place(x=50,y=50)

frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)

heading=Label(frame,text='sign in',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=5)
##############=====================================

def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')
user = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

###########=========================================
def on_enter(e):
    code.delete(0, 'end')

def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'password')


code = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)


Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

##################################################################

Button(frame,width=39,pady=7,text='sign in',bg='#57a1f8',fg='white',border=0,command=signin).place(x=35,y=204)
label=Label(frame,text="Don't have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=75,y=270)

sign_up= Button(frame,width=6,text='sign up',border=0,bg='white',cursor='hand2',fg='#57a1f8',)
sign_up.place(x=215,y=270)

root.mainloop()



