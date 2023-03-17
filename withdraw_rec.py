from tkinter import*
from subprocess import call
from datetime import datetime
from time  import strftime
from tkinter import messagebox
from subprocess import call
import tkinter.messagebox as MessageBox
import mysql.connector as con




db=con.connect(
            host="localhost",
            user="root",
            password="",
            port=3306,
            database="mybms"
            )



class Table:
     
    def __init__(self,root):
         
        # code for creating table
        for i in range(l):
            for j in range(m):
                if j==6:
                    continue
                 
                self.e = Entry(root, width=45, fg='black',
                               font=('Arial',10,'bold'))
                if(i==0):
                    self.e.config(background='#5050CE',foreground='white')
                 
                self.e.grid(row=i, column=j)
                self.e.insert(END, d[i][j])
                self.e.config(relief='sunken')
                
                
                
cursur=db.cursor()
q="""select * from withdraw"""
cursur.execute(q)
d=cursur.fetchall()

attribut=("ID","CURRENT BALANCE","WITHDRAW AMOUTN","NEW BALANCE","DATE")
d.insert(0,attribut)
l=len(d)
m=len(d[0])




root=Tk()
root.title("WITHDRAW RECOND")
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry(f"{width}x{height}")
root.config(background='#5050CE')

Table(root)
     
root.mainloop()