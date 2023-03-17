from tkinter import*
from subprocess import call
from datetime import date

import tkinter.messagebox as MessageBox
from subprocess import call
import login as log
import mysql.connector as con
from datetime import date


db=con.connect(
host="localhost",
user="root",
password="",
port=3306,
database="mybms"
)


def account():
    var=0
    
    
     
    root=Tk()
    root.title("New Account")
    
    
   
    root.attributes('-fullscreen', True)
    
    fone=Frame(root,height=100,background='white').pack(fill=X)
    ftwo=Frame(root,height=1000,background='#5449F1').pack(fill=X)
    
    ##lavel
    acc=Label(root,text="Withdraw Balance",font=("lato",40,"bold"),foreground='#5449F1',background='white').place(relx=.5,rely=.05,anchor=CENTER)
   


    
   
    idl=Label(root,text="Account ID : ",background='#5449F1',foreground='white',font=('times romans',20,'bold')).place(relx=.03,rely=.2)
    id_e=Entry(root,width=30,font=('times romans',15,'bold'))
    id_e.place(relx=.2,rely=.21)
    
    
    first=Label(root,text="First Name : ",background='#5449F1',foreground='white',font=('times romans',20,'bold')).place(relx=.03,rely=.3)
    first_e=Entry(root,width=30,font=('times romans',15,'bold'))
    first_e.place(relx=.2,rely=.31)
    
    last=Label(root,text="Last Name : ",background='#5449F1',foreground='white',font=('times romans',20,'bold')).place(relx=.03,rely=.4)
    last_e=Entry(root,width=30,font=('times romans',15,'bold'))
    last_e.place(relx=.2,rely=.41)
    
    current_balace=Label(root,text="Curent Balance : ",background='#5449F1',foreground='white',font=('times romans',20,'bold')).place(relx=.03,rely=.5)
    cbalance_e=Entry(root,width=30,font=('times romans',15,'bold'))
    cbalance_e.place(relx=.2,rely=.51)
    
    withdraw=Label(root,text="Withdraw  Balance: ",background='#5449F1',foreground='white',font=('times romans',20,'bold')).place(relx=.03,rely=.6)
    wbalance_e=Entry(root,width=30,font=('times romans',15,'bold'))
    wbalance_e.place(relx=.2,rely=.61)
    new_balance=Label(root,text="New Balance : ",background='#5449F1',foreground='white',font=('times romans',20,'bold')).place(relx=.03,rely=.7)
    newbalance_e=Entry(root,width=30,font=('times romans',15,'bold'))
    newbalance_e.place(relx=.2,rely=.71)
    
    
    
   
    
            
        
      
    
        
       
        
        
  
    
    
    
    
    
    
    
    
    
    #submitbutton
    def search():
        
        Id=id_e.get()
        
        if Id=="":
            MessageBox.showwarning("Illegal insertion","ID required fill up")
            return
        elif Id.isdigit()==False:
            MessageBox.showerror("Invalid ID","Inserted Wrong format Id !\nId containg only digit")
            return
        else:
            cursor=db.cursor()
            query="""select first_name,last_name,balance from account where id=%s"""
            cursor.execute(query,(Id,))
            result=cursor.fetchall()
            
            if(len(result)==0):
                MessageBox.showwarning("Invalid Id","No result found,Plz insert correct Id")
                return
            else:
                
                first_e.delete(0,END)
                first_e.insert(END,result[0][0])
                
                last_e.delete(0,END)
                last_e.insert(END,result[0][1])
                
                cbalance_e.delete(0,END)
                cbalance_e.insert(END,result[0][2])
    
    
    
    def submit():
         
          wb=wbalance_e.get()
          cb=cbalance_e.get()
          Id=id_e.get()
          
          
          if wb=="":
              MessageBox.showwarning("Invalid Withdraw balnce","Plz insert withdraw amount")
              return
          elif wb.isdigit()==False:
              MessageBox.showwarning("Invalid Balnce","Balace contain only digt\nPlz insert correct balance")
              return
          elif int(wb)>int(cb):
              MessageBox.showwarning("Amount Exceeded","Wirhdraw Balance amounut Exceeded current amount")
              return
          else:
               newBalance=int(cb)-int(wb)
               
             
               newbalance_e.delete(0,END)
               newbalance_e.insert(END,newBalance)
               
    def confirm():
        
        
        
        if(id_e.get()=="" or newbalance_e.get()=="") :
             MessageBox.showinfo("Withdreap process","Search and Submit first ")
             return 0
        else:
            
            
            Id=id_e.get()
            cb=cbalance_e.get()
            cbal=int(cb)
            wb=wbalance_e.get()
            wbal=int(wb)
            nb=newbalance_e.get()
            nbal=int(nb)
            
            
        
            
            
            
            cursor=db.cursor()
            query="""UPDATE account set balance=%s where id=%s """
            data=(nbal,Id)
            cursor.execute(query,data)
            db.commit()
            
            
            sql= (
                "INSERT INTO withdraw(id,current_balance,withdraw_amount,new_balnce,date)"
                "VALUES (%s, %s, %s,%s,%s)"
                )

            d=date.today()
            data = (Id,cbal,wbal,nbal,d)
                
            cursor.execute(sql,data)
            db.commit()
            
            id_e.delete(0,END)
            first_e.delete(0,END)
            last_e.delete(0,END)
            cbalance_e.delete(0,END)
            wbalance_e.delete(0,END)
            newbalance_e.delete(0,END)
            
            
            top=Toplevel(root)
            top.geometry('720x730+390+20')
            top.title(" Withdraw Balance!")
            top.config(bg='#5449F1')
            
            text1="Successfully! "+str(wb)+"TK Withdraw from acconut Id: "+str(Id)+"TK\n Current balance is "+str(nbal)+"TK\n Thank you !"
            Label(top,text=text1,font=("lato",18,"bold"),foreground='#F9F9FB',background='#5449F1').place(relx=.05,rely=.2)
            top.mainloop()
                
        
        
        
               
               


          
          
          
          
          
        
         
                
            
            
            
            
        
    
        
    
        
        
        
    submit_btn=Button(root,text="Submit",width=18,font=("times romans",15,'bold'),foreground='#5449F1',bd=8,command=submit).place(relx=.7,rely=.35,anchor=CENTER)
    clear_btn=Button(root,text="Search",width=18,font=("times romans",15,'bold'),foreground='#5449F1',bd=8,command=search).place(relx=.7,rely=.25,anchor=CENTER)
    clear_btn=Button(root,text="Confirm",width=18,font=("times romans",15,'bold'),foreground='#5449F1',bd=8,command=confirm).place(relx=.7,rely=.45,anchor=CENTER)
    quite_btn=Button(root,text="Quit",width=18,font=("times romans",15,'bold'),foreground='#5449F1',bd=8,command=root.destroy).place(relx=.7,rely=.55,anchor=CENTER)
    
    
    
    root.mainloop()
    
    
    
    
    
if __name__=="__main__":
    account()
