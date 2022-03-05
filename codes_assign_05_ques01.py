
from tkinter import*

#Function for finding gst rate
def find_gst():
    org_cost=int(org_priceField.get())
    net_cost=int(net_priceField.get())
    gst_rate=((net_cost - org_cost) * 100) / org_cost
    print("the original cost is: ",org_cost)
    print("the net cost is : ",net_cost)
    print("the gst rate is : ",gst_rate)
    gst_rateField.insert(12, str(gst_rate) + "%")

#function for clearing all the enteries
def clear_all():
    org_priceField.delete(0,END)
    net_priceField.delete(0,END)
    gst_rateField.delete(0,END)

#driver code
win=Tk()
win.configure(background='light green')
win.geometry('500x500')
win.title("GST RATE FINDER")
lbl_1=Label(win,text='ENTER ORIGINAL PRICE',bg='yellow',relief='ridge',padx=3,pady=3,bd=3,font=('calibre',12,'bold','underline'))
lbl_1.grid(row=1,column=1,padx=10,pady=10)
lbl_2=Label(win,text="ENTER NET PRICE",bg='yellow',relief='ridge',padx=3,pady=3,bd=3,font=('calibre',12,'bold','underline'))
lbl_2.grid(row=2,column=1,padx=10,pady=10)
but_1=Button(win,text="Calculate",padx=3,pady=3,bg='light grey',relief='sunken',bd=3,font=('calibre',12),command=find_gst,activebackground='light yellow')
but_1.grid(row=3,column=2,padx=10,pady=10)
lbl_3=Label(win,text="GST RATE IS",bg='yellow',relief='ridge',padx=3,pady=3,bd=3,font=('calibre',12,'bold','underline'))
lbl_3.grid(row=4,column=1,padx=10,pady=10)
but_2=Button(win,text="Clear",padx=3,pady=3,bg='light grey',relief='sunken',bd=3,font=('calibre',12),command=clear_all,activebackground='light yellow')
but_2.grid(row=5,column=2,padx=10,pady=10)
org_priceField=Entry(win)
org_priceField.grid(row=1,column=2,padx=10,pady=10)
net_priceField=Entry(win)
net_priceField.grid(row=2,column=2,padx=10,pady=10)
gst_rateField=Entry(win)
gst_rateField.grid(row=4,column=2,padx=10,pady=10)
win.mainloop()
