#tkinter ve import etme

form=tk.Tk()
form.title('tkinter ders')
etiket=tk.Label(text='Tkinter dersleri')
etiket.pack()
etiket2=tk.Label(form,text='label2')
etiket2.pack()
form.mainloop()

#-----2.Bölüm---------

from tkinter import *
from tkinter import messagebox

def Ok():
    uname=e1.get()
    password=e2.get()
    if(uname==""and password==""):
        messagebox.showinfo("Lutfen bos birakmayiniz")
    elif(uname=="admin"and password=="123"):
        messagebox.showinfo("Giris Basarili")
    else:
        messagebox.showinfo("Hatali giris")


root=Tk()
root.title=("Login")
root.geometry("300x200")
global e1
global e2
global e3
global e4
Label (root,text="Username").place(x=10,y=10)
Label(root,text="Password").place(x=10,y=40)
e1=Entry(root)
e1.place(x=140,y=10)
e2=Entry(root)
e2.place(x=140,y=40)
e2.config(show="*")
Button(root,text="Login",command=Ok, height=3,width=13).place(x=10,y=100)
root.mainloop()






















