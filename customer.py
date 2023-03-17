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



def main():
    
    root=Tk()
    root.attributes('-fullscreen', True)
    
    fone=Frame(root,height=100,background='white').pack(fill=X)
    ftwo=Frame(root,height=1000,background='#5449F1').pack(fill=X)
    
    
    lone=Label(root,text="Client Controll",font=("lato",40,"bold"),foreground='#5449F1',background='white').place(relx=.5,rely=.05,anchor=CENTER)  
    
    
    
    
    def show_info():
        
        call(["python","showcurrentBalance.py"])
        quit()
    
    def withdraw_rec():
        call(["python","customer_withdraw_rec.py"])
        quit()
    
    
    
    def Deposite_rec():
        call(["python","customer_deposite _record.py"])
        quit()
    
    def update_onfo():
        call(["python","update_customer_info.py"])
        quit()
        
        
        
        
        
        
        
        

        

    
    
    
    
    
    show=Button(root,text="Show Current Balance ",width=25,bd=5,font=('times romans',15,'bold'),command=show_info).place(relx=.4,rely=.2)
    
    
    withdeow=Button(root,text="Show Withdraw Record",width=25,bd=5,font=('times romans',15,'bold'),command=withdraw_rec).place(relx=.4,rely=.3)
    deposite=Button(root,text="Show Deopiste record",width=25,bd=5,font=('times romans',15,'bold'),command=Deposite_rec).place(relx=.4,rely=.4)
    change_info=Button(root,text="Update information",width=25,bd=5,font=('times romans',15,'bold'),command=update_onfo).place(relx=.4,rely=.5)
    quit=Button(root,text="Quit",width=25,bd=5,font=('times romans',15,'bold'),command=root.destroy).place(relx=.4,rely=.7)

    root.mainloop()
    
    
if __name__=="__main__":
    main()
    
    
    

   
    



