from tkinter import *
import calendar

#function for clearing inputs an outputs
def clear_all():
    en_1.delete(0,END)


#function for printing calender
def print_cal():
    win2=Tk()
    win2.geometry('700x700')
    win2.configure(background='light yellow')
    win2.title("Calender output")
    year=int(en_1.get())
    cal_pr=calendar.calendar(year)
    lbl_3=Label(win2,text=cal_pr)
    lbl_3.pack()
    win2.mainloop()

win=Tk()
win.geometry('500x500')
win.configure(background='light yellow')
win.title("Calender")
lbl_1=Label(win,text="CALENDER",relief='ridge',bd=4,bg='light green',font=('calibre',20,'bold','underline'),padx=4,pady=4)
lbl_1.grid(row=1,column=1,pady=15,padx=50)
lbl_2=Label(win,text="Enter the year of which you want to view the calender",relief='sunken',bd=3,bg='light grey',font=('calibre',15),padx=3,pady=3)
lbl_2.grid(row=2,column=0,padx=10,pady=30)
but_1=Button(win,text="Print",relief='sunken',bd=3,bg='light grey',font=('calibre',15),padx=3,pady=3,activebackground='light blue',command=print_cal)
but_1.grid(row=3,column=1,pady=20)
en_1=Entry(win,font=('calibre',15))
en_1.grid(row=2,column=1,pady=30)
but_2=Button(win,text="clear",relief='sunken',bd=3,bg='light grey',command=clear_all, font=('calibre',15),padx=3,pady=3,activebackground='light blue')
but_2.grid(row=5,column=1)
win.mainloop()