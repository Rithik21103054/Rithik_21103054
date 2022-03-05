from tkinter import *
def sum():
    num_1=float(en_1.get())
    num_2=float(en_2.get())
    ans=num_1 + num_2
    en_3.insert(12, str(ans))

def clear_all():
    en_1.delete(0,END)
    en_2.delete(0,END)
    en_3.delete(0,END)

def subtract():
    num_1=float(en_1.get())
    num_2=float(en_2.get())
    ans=num_1 - num_2
    en_3.insert(12, str(ans))

def multiply():
    num_1=float(en_1.get())
    num_2=float(en_2.get())
    ans=num_1 * num_2
    en_3.insert(12, str(ans))

def divide():
    num_1=float(en_1.get())
    num_2=float(en_2.get())
    ans=num_1 / num_2
    en_3.insert(12, str(ans))


win=Tk()
win.configure(background='light yellow')
win.geometry('600x600')
win.title('Basic Calculator')
lbl_1=Label(win,text="CALCULATOR",relief='raised',bd=5,padx=5,pady=5,bg='light green',font=('calibre',20,'bold','underline'))
lbl_1.grid(row=0,column=1,padx=10,pady=10)
lbl_2=Label(win,text="Enter the first number",relief='ridge',bd=3,padx=5,pady=5,bg='light blue',font=('calibre',15,'bold'))
lbl_2.grid(row=1,column=0,padx=5,pady=10)
lbl_3=Label(win,text="Enter the second number",relief='ridge',bd=3,padx=5,pady=5,bg='light blue',font=('calibre',15,'bold'))
lbl_3.grid(row=2,column=0,padx=5,pady=10)
lbl_4=Label(win,text="RESULT",relief='ridge',bd=3,padx=5,pady=5,bg='light blue',font=('calibre',15,'bold'))
lbl_4.grid(row=7,column=0,padx=5,pady=10)
en_1=Entry(win)
en_1.grid(row=1,column=1,padx=5,pady=10,columnspan=4)
en_2=Entry(win)
en_2.grid(row=2,column=1,padx=5,pady=10,columnspan=4)
en_3=Entry(win)
en_3.grid(row=7,column=1,padx=5,pady=10,columnspan=4)
but_1=Button(win,text='add(+)',relief='sunken',bd=3,bg='light grey',command=sum)
but_1.grid(row=3,column=1,padx=5,pady=10)
but_2=Button(win,text='subtract(-)',relief='sunken',bd=3,bg='light grey',command=subtract)
but_2.grid(row=4,column=1,padx=5,pady=10)
but_3=Button(win,text='multiply(*)',relief='sunken',bd=3,bg='light grey',command=multiply)
but_3.grid(row=5,column=1,padx=5,pady=10)
but_4=Button(win,text='divide(/)',relief='sunken',bd=3,bg='light grey',command=divide)
but_4.grid(row=6,column=1,padx=5,pady=10)
but_5=Button(win,text="clear",relief='sunken',bd=3,bg='light grey',command=clear_all)
but_5.grid(row=8,column=1,padx=5,pady=10)
win.mainloop()