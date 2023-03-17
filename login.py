from tkinter import*
from subprocess import call
from datetime import datetime
from time  import strftime
from tkinter import messagebox
from subprocess import call
import tkinter.messagebox as MessageBox
import mysql.connector as con


##Authority

db=con.connect(
            host="localhost",
            user="root",
            password="",
            port=3306,
            database="mybms"
            )





def login():
    root=Tk()
    root.attributes('-fullscreen', True)
   
     
    #design-------------------------------------------------------------------
    
    #frame
    fone=Frame(root,height=100,bg="white").pack(fill=X)
    ftwo=Frame(root,height=700,bg='#5449F1').pack(fill=X)
    fthree=Frame(root,height=100,bg='black').pack(fill=X)



    #label
    lone=Label(root,text="$ Bank Management System $",font=("lato",40,"bold"),foreground='#5449F1',background='white').place(relx=.5,rely=.05,anchor=CENTER)  
    l_login=Label(root,text="~ LOGIN ~",font=("times romans",35,"bold"),foreground='white',background='#5449F1').place(relx=.5,rely=.2,anchor=CENTER)

    id=Label(root,text='Client/Authority  Id',foreground='white',background='#5449F1',font=('times romans',15,'bold')).place(relx=.2,rely=.3)
    e_id=Entry(root,width=60,font=('times romans',12,'bold'))
    e_id.place(relx=.4,rely=.3)
    email=Label(root,text="Client/Authority E-mail",foreground='white',background='#5449F1',font=('times romans',15,'bold')).place(relx=.2,rely=.4)
    e_email=Entry(root,width=60,font=('times romans',12,'bold'))
    e_email.place(relx=.4,rely=.4)

    password=Label(root,text="Client/Authority Password",foreground='white',background='#5449F1',font=('times romans',15,'bold')).place(relx=.2,rely=.5)
    e_password=Entry(root,width=60,font=('times romans',12,'bold'),show="*")
    e_password.place(relx=.4,rely=.5)



    #functional funciton
    
    
    def choice():
        
        #variable----------------------------------  
        
        it=inp.get()
        Id=e_id.get()
        Email=e_email.get()
        Password=e_password.get()
        
        
        
         
        # Cheking id,gmail,password.................................
        
        if (Id=="" or Email=="" or Password==""):
            MessageBox.showwarning("INVALID INFORMATION", "All Fields are Required")
        elif(Id.isdigit()==False):
                MessageBox.showwarning("ILLEGAL INFORMATION", "Sorry ! inserted incorrect format Id ")
                return
        
        else:
            if(it==2):
                
                cursor=db.cursor()
                cursor.execute("SELECT MIN(id),MAX(id) from account")
                account_id=cursor.fetchone()
                
                x=int(account_id[0])
                y=int(account_id[1])
                
                
            
                if(int(Id)<x or int(Id)>y):
                    MessageBox.showinfo("INVALID INFORMATION", "Sorry ! Can't find Acount")
                    return
                    
                
                    
               
                query="""select gmail,password from account where id=%s"""
                cursor.execute(query,(Id,))
                 
                result=cursor.fetchall()
                dresult=result[0]
               
                
                
                if(  dresult[0]!=Email or dresult[1]!=Password ):
                     MessageBox.showinfo("LOGIN SECURITY","Unsucesfull attempt! incorrect information")
                     return
                else:
                    MessageBox.showinfo("LOGIN SECURITY","Sucessful ! Welcome to Client side")
                    
                    call(["python",'customer.py'])
                    quit()
                    
                   
                   
    
            elif(it==1):
                
                
                cursor1=db.cursor()
                cursor1.execute("SELECT MIN(id),MAX(id) from employee")
                account_id=cursor1.fetchone()
                
                
                
                x=int(account_id[0])
                y=int(account_id[1])
                
                
            
                if(int(Id)<x or int(Id)>y):
                    MessageBox.showinfo("Invalid information", "Sorry ! Can't find Acount")
                    return
                
                
                
                query="""select email,password from employee where id=%s"""
                cursor1.execute(query,(Id,))
                 
                result=cursor1.fetchall()
                dresult=result[0]
               
                
                
                if(  dresult[0]!=Email or dresult[1]!=Password ):
                     MessageBox.showinfo("LOGIN SECURITY","Unsucesfull attempt! incorrect  information")
                     return
                   
                else:
                    MessageBox.showinfo("LOGIN SECURITY","Sucessful ! Welcome to Office")
                    
                    call(["python",'authority.py'])
                    quit()
     
     
     
     
     
     
     #Refresh login information               
    def refresh():
        e_id.delete(0,END)
        e_email.delete(0,END)
        e_password.delete(0,END)
    
    def passret():
         call(["python",'password.py'])
         quit()
         
         
     
        
        
    
        
    
        
                   
                  
                
                
                
                
                
                
                
                

    #Authoirty of customer_ratiobutton
    inp=IntVar(root)
    inp.set(1)
    Radiobutton(root,text="Authority",variable=inp,value=1,background='#5449F1',foreground='black',font=('times romans',20,'bold')).place(relx=.35,rely=.6)
    Radiobutton(root,text="Client",variable=inp,value=2,background='#5449F1',foreground='black',font=('times romans',20,'bold')).place(relx=.53,rely=.6)



    
    
    
        
       
        
        
    #Funcitonal Button   
    submit_btn=Button(root,text="Submit",width=20,font=("times romans",15,'bold'),foreground='#5449F1',bd=8,command=choice).place(relx=.49,rely=.75,anchor=CENTER)
    clear_btn=Button(root,text="Refresh",width=18,font=("times romans",15,'bold'),foreground='#5449F1',bd=8,command=refresh).place(relx=.28,rely=.75,anchor=CENTER)
    quite_btn=Button(root,text="Quit",width=18,font=("times romans",15,'bold'),foreground='#5449F1',bd=8,command=root.destroy).place(relx=.7,rely=.75,anchor=CENTER)
    Label(root,text="Password forgetted ??  Click to Retrieve ",background='#5449F1',foreground='white',font=('times romans',20,'bold')).place(relx=.2,rely=.85)
    Button(root,text="Click",width=12,font=("times romans",10,'bold'),foreground='#01010C',command=passret).place(relx=.6,rely=.87,anchor=CENTER)

     
    root.mainloop()
    
    
    
    
    
    
if __name__=="__main__":
    login()

    

