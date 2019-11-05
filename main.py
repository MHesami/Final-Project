import tkinter as tk
from tkinter import messagebox
from PhoneContact import Contact, Person
    
def insert_contact():
    c =Contact()
    p=Person()
    if e1.get()!="" and e2.get()!= "" and e3.get()!="":
        p.name=e1.get()
        p.family=e2.get()
        n= p.name+' '+ p.family
        c.add(e3.get()+': '+n)
        e1.delete(0, tk.END)
        e2.delete(0, tk.END)
        result=n + " was inserted"
        lbl.config(text=result)
    else:
        lbl.config(bg="red")
        lbl.config(text="You don't enter one or more Fields")

def show_contacts():
    c =Contact()
    print(c.show_all())
    quote = c.show_all()
    T.insert(tk.END, quote)
    
def dial():
        try:
            c =Contact()
            result = "Dialing ...: "+e4.get()+"\n"+ c.get_contact(e4.get()) 
            lbl.config(bg="green")
        except:
            lbl.config(bg="red")
            result="There is not any number, Please Enter a number"
        lbl.config(text=result)



    
if __name__=="__main__":
    c= Contact()

    master = tk.Tk()
    tk.Label(master, text="You are able to add a new contact below :",fg = "red",width=40).grid(row=0,column=0)
    tk.Label(master, text="First Name",width=15).grid(row=1,column=0,sticky=tk.W)
    tk.Label(master, text="Last Name",width=15).grid(row=2,column=0,sticky=tk.W)
    tk.Label(master, text="Number",width=15).grid(row=3,column=0,sticky=tk.W)
    
    e1 = tk.Entry(master,width=25)
    e2 = tk.Entry(master,width=25)
    e3 = tk.Entry(master,width=25)
    e4 = tk.Entry(master,width=33)
    
    
    
    e1.grid(row=1, column=0,sticky=tk.E)
    e2.grid(row=2, column=0,sticky=tk.E)
    e3.grid(row=3, column=0,sticky=tk.E)
    e4.grid(row=7, column=0,sticky=tk.E)
  
    S = tk.Scrollbar(master)
    T = tk.Text(master, height=5, width=33)
    S.grid(row=6, column=0,sticky=tk.E)
    T.grid(row=6,column=0,sticky=tk.W)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)

    lbl= tk.Label(master, text="NO dial", height=5, width=39)
    lbl.grid(row=8, column=0)
    
    tk.Button(master, text='Quit', command=master.destroy,width=40,bg = "silver").grid(row=9, column=0,  sticky=tk.W,)
    tk.Button(master, text='Insert', command=insert_contact,width=18,bg = "silver").grid(row=4, column=0, sticky=tk.W, pady=4)
    tk.Button(master, text='Show Contacts', command=show_contacts,width=18,bg = "silver").grid(row=4, column=0, sticky=tk.E, pady=4)
    tk.Button(master, text='Dial', command=dial,width=10,bg = "silver").grid(row=7, column=0, sticky=tk.W, pady=4)
    master.mainloop()

    tk.mainloop()
