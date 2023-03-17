from tkinter import*
from subprocess import call
from datetime import datetime
from time  import strftime
from tkinter import messagebox
from subprocess import call


##Authority

def main():
    root=Tk()
    root.title("Authority page")
    root.attributes('-fullscreen', True)
    
    fone=Frame(root,height=100,background='white').pack(fill=X)
    ftwo=Frame(root,height=1000,background='#5449F1').pack(fill=X)
    lone=Label(root,text="Authority",font=("lato",40,"bold"),foreground='#5449F1',background='white').place(relx=.5,rely=.05,anchor=CENTER)  

    
    
    
    def account():
        
        call(["python","create_acc.py"])
        quit()
    
    def withdraw():
        call(["python","withdraw.py"])
        quit()
        
    def Deposite():
        call(["python","deposite.py"])
        quit()
    
    def withdraw_record():
        call(["python","withdraw_rec.py"])
        quit()
        
    def deposite_record():
        call(["python","withdraw_rec.py"])
        quit()
        
        
        
        
        
    def add_employee():
        
        call(["python","employye.py"])
        quit()
        
    def customer_record():
        call(["python","account_rec.py"])
        quit()
    
    def employee_recond():
        call(["python","emplyee_rec.py"])
        quit()
    
    
    def update_customer():
        call(["python","update_customer_info.py"])
        quit()
    
    
    def update_employee_info():
        call(["python","update_employee_info.py"])
        quit()
        
        
        
        
    
    
    
    
        
        
    
        
    def find_information():
        
        call(["python","search.py"])
        quit()
        
        
        
    
    create=Button(root,text="Create New Account ",width=25,bd=5,font=('times romans',15,'bold'),command=account).place(relx=.2,rely=.3)
    Withdraw=Button(root,text="Withdraw",width=25,bd=5,font=('times romans',15,'bold'),command=withdraw).place(relx=.2,rely=.4)
    deposite=Button(root,text="Deposite ",width=25,bd=5,font=('times romans',15,'bold'),command=Deposite).place(relx=.2,rely=.5)
    add_emp=Button(root,text="Add Employee",width=25,bd=5,font=('times romans',15,'bold'),command=add_employee).place(relx=.2,rely=.6)
    wdr=Button(root,text="Withdraw record",width=25,bd=5,font=('times romans',15,'bold'),command=withdraw_record).place(relx=.2,rely=.7)
    dr=Button(root,text="Deposite record",width=25,bd=5,font=('times romans',15,'bold'),command=deposite_record).place(relx=.2,rely=.8)
   
    
    cu_rec=Button(root,text="Customer record",width=25,bd=5,font=('times romans',15,'bold'),command=customer_record).place(relx=.6,rely=.3)
    record=Button(root,text="Employee record",width=25,bd=5,font=('times romans',15,'bold'),command=employee_recond).place(relx=.6,rely=.4)
    record=Button(root,text="Update customer information",width=25,bd=5,font=('times romans',15,'bold'),command=update_customer).place(relx=.6,rely=.5)
    updateinformation=Button(root,text="Update employee information",width=25,bd=5,font=('times romans',15,'bold'),command=update_employee_info).place(relx=.6,rely=.6)
    serch_information=Button(root,text="Search information",width=25,bd=5,font=('times romans',15,'bold'),command=find_information).place(relx=.6,rely=.7)
    quit=Button(root,text="Quit",width=25,bd=5,font=('times romans',15,'bold'),command=root.destroy).place(relx=.6,rely=.8)

    root.mainloop()
    


if __name__=="__main__":
    main()
    
    
    
    