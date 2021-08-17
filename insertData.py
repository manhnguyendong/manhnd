import psycopg2
from tkinter import *
from tkinter.ttk import *
conn = psycopg2.connect(database='Bill', user='postgres', password='manh123')
conn.autocommit = True
win = Tk()
cursor = conn.cursor()
def insertData():
    conn = psycopg2.connect(database='Bill', user='postgres', password='manh123')
    cur = conn.cursor()
    cur.execute("INSERT INTO HANGHOA VALUES('%s', '%s')"%(HANGHOA.get(), Dongia.get()))
    cur.close()
    conn.commit()
    conn.close()
    status.set('Data added Succesfully')
status = StringVar()
HANGHOA = StringVar()
Dongia = StringVar()

def drawEnterframe():
    ten_hang_hoa = Label(win, text='Enter name goods').place(x='0', y = '50')
    Enter1 = Entry(win, textvariable=HANGHOA).place(x='100', y='50')
    Don_gia = Label(win, text='Enter price').place(x='0', y='100')
    Enter2 = Entry(win, textvariable=Dongia).place(x='100', y='100')
    Status = Label(win, text='', textvariable=status).place(x='150', y='150')

def Submit():
    hanghoa = HANGHOA.get()
    dongia = Dongia.get()
    insertData()
    print ("Ten hang hoa : " + hanghoa) 
    print ("Don gia san pham :" + dongia)
    HANGHOA.set("")
    Dongia.set("")

#driver_code
def main():
    win.geometry('300x300')
    win.title('Bảng cập nhật hàng hóa')
    win.maxsize(height=300, width=300)
    drawEnterframe()
    btn1 = Button(win, text='Enter', command=Submit).place(x='100', y='150')
    win.mainloop()

if __name__ == "__main__":
    main()

conn.close()