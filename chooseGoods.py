import psycopg2
from tkinter import *
from tkinter.ttk import *


win = Tk()
win.geometry('500x500')
frm = Frame(win, height=100, width=100)
frm.pack(padx=10)


textFind = StringVar()

def Find():
    text = textFind.get()
    conn = psycopg2.connect(
    database="Bill", user='postgres', password='manh123')
    cursor = conn.cursor()
    sql = f"SELECT * FROM HANGHOA WHERE TENandSize ILIKE '{text}%'"
    cursor.execute(sql)
    rows = cursor.fetchall()
    total = cursor.rowcount
    print ("Total Data Entries: " + str(total))  
    tv = Treeview(frm , columns=(1, 2), show = "headings", height=20)
    tv.pack()  
    for i in rows:
        tv.insert('', 'end', values=i)
    tv.heading(1, text='Ten hang')
    tv.heading(2, text='Don gia')
    conn.close()

find = Label(win, text='FIND').pack(side=BOTTOM)
EntryFind = Entry(win, textvariable=textFind).pack(side=BOTTOM)
btnFind = Button(win, text='Click to find', command=Find).pack(side=BOTTOM)


mainloop()