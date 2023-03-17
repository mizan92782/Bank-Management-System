from tkinter import*
from subprocess import call
from datetime import datetime
from time  import strftime
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
    
    
     
    root=Tk()
    root.title("New Account")
    
    
   
    root.attributes('-fullscreen', True)
    
    fone=Frame(root,height=100,background='white').pack(fill=X)
    ftwo=Frame(root,height=1000,background='#5449F1').pack(fill=X)
    
    ##lavel
    acc=Label(root,text="Create New Account",font=("lato",40,"bold"),foreground='#5449F1',background='white').place(relx=.5,rely=.05,anchor=CENTER)
   

    
    
  
    
    
    
    
    
    
    ### information------------------------
    idno=IntVar()
    
   
   
    
    cursor=db.cursor()
    cursor.execute('SELECT MAX(id) FROM account')
    id=cursor.fetchone()[0]
    
   
    
    idno.set(id+1)
    idl=Label(root,text="Account ID : ",background='#5449F1',foreground='white',font=('times romans',20,'bold')).place(relx=.03,rely=.2)
    ide=Entry(root,textvariable=idno,width=30,font=('times romans',15,'bold'))
    ide.place(relx=.15,rely=.21)
    
    
    first=Label(root,text="First Name : ",background='#5449F1',foreground='white',font=('times romans',20,'bold')).place(relx=.03,rely=.3)
    first_e=Entry(root,width=30,font=('times romans',15,'bold'))
    first_e.place(relx=.15,rely=.31)
    
    last=Label(root,text="Last Name : ",background='#5449F1',foreground='white',font=('times romans',20,'bold')).place(relx=.03,rely=.4)
    last_e=Entry(root,width=30,font=('times romans',15,'bold'))
    last_e.place(relx=.15,rely=.41)
    
    nid=Label(root,text="NID : ",background='#5449F1',foreground='white',font=('times romans',20,'bold')).place(relx=.03,rely=.5)
    nid_e=Entry(root,width=30,font=('times romans',15,'bold'))
    nid_e.place(relx=.15,rely=.51)
    
    contact=Label(root,text="Number : ",background='#5449F1',foreground='white',font=('times romans',20,'bold')).place(relx=.5,rely=.2)
    contact_e=Entry(root,width=30,font=('times romans',15,'bold'))
    contact_e.place(relx=.6,rely=.21)
    
    gmail=Label(root,text="G-maiL : ",background='#5449F1',foreground='white',font=('times romans',20,'bold')).place(relx=.5,rely=.3)
    gmail_e=Entry(root,width=30,font=('times romans',15,'bold'))
    gmail_e.place(relx=.6,rely=.31)
    
    
    password=Label(root,text="Password : ",background='#5449F1',foreground='white',font=('times romans',20,'bold')).place(relx=.5,rely=.4)
    password_e=Entry(root,width=30,font=('times romans',15,'bold'))
    password_e.place(relx=.6,rely=.41)
    
    Address=Label(root,text="City : ",background='#5449F1',foreground='white',font=('times romans',20,'bold')).place(relx=.5,rely=.5)
    address_e=Entry(root,width=30,font=('times romans',15,'bold'))
    address_e.place(relx=.6,rely=.51)
    
    
    
    gender=StringVar(root)
    gender.set('Male')
    
    Radiobutton(root,text="Male",variable=gender,value="Male",background='#5449F1',foreground='black',font=('times romans',20,'bold')).place(relx=.5,rely=.6)
    Radiobutton(root,text="Female",variable=gender,value="Female",background='#5449F1',foreground='black',font=('times romans',20,'bold')).place(relx=.6,rely=.6)
    Radiobutton(root,text="others",variable=gender,value="Others",background='#5449F1',foreground='black',font=('times romans',20,'bold')).place(relx=.7,rely=.6)
    
    
    def add_dbms():
        
        
        #getvalue
     
        
        id_no=idno.get()
        fname=first_e.get()
        lname=last_e.get()
        Nid=nid_e.get()
      
        number=contact_e.get()
        g_mail=gmail_e.get()
        City=address_e.get()
        Gender=gender.get()
        Password=password_e.get()
        
        
        if(id_no=="" or fname=="" or number== " " or Nid=="" or g_mail=="" or gender=="" or City=="" or Password=="" ):
            MessageBox.showinfo("New account create", "Sorry ! filled up all field to created accont")
        else:
            cursor=db.cursor()
            sql= (
            "INSERT INTO account(id, first_name,last_name,nid,number,gmail,password,city,gender,date,balance)"
            "VALUES (%s, %s, %s,%s, %s, %s,%s, %s,%s,%s,%s)"
            )

            d=date.today()
            data = (id_no, fname,lname,Nid,number,g_mail,Password,City,Gender,d,0)
            
            cursor.execute(sql,data)

            # Commit your changes in the database
            db.commit()
            
            top=Toplevel(root)
            top.geometry('670x700+50+50')
            top.title(" Office !")
            top.config(bg='#5449F1')

            lone=Label(top,text="WellCome!",background='#5449F1',fg='white',font=('Times and romans',30,'bold')).place(relx=.3,rely=.1)
            abc="Hi' " +fname+" "+lname+".Wellcome to you as our business parther with mutual trust,\nWe ensure you about your properties security"
            ltwo=Label(top,text=abc,background='#5449F1',fg='white',font=('Times and romans',13,'bold')).place(relx=0.05,rely=.3)
            
            ltree=Label(top,text="Thank you for Believe us!",background='#5449F1',fg='white',font=('Times and romans',30,'bold')).place(relx=.1,rely=.5)
            
            
            x=idno.get()
            ide.delete(0,END)
            ide.insert(0,x+1)
            
            refresh()
            top.mainloop()
            
            
        
      
    
        
       
        
        
  
    
    
    
    
    
    
    
    
    
    #submitbutton
    def refresh():
        
        first_e.delete(0,END)
        last_e.delete(0,END)
        nid_e.delete(0,END)
        contact_e.delete(0,END)
        gmail_e.delete(0,END)
        password_e.delete(0,END)
        address_e.delete(0,END)
        
    
        
    def loginpart():
        root.destroy()
        call(['python','authority.py'])
        quit()
        
        
        
        
    submit_btn=Button(root,text="Submit",width=20,font=("times romans",15,'bold'),foreground='#5449F1',bd=8,command=add_dbms).place(relx=.49,rely=.75,anchor=CENTER)
    clear_btn=Button(root,text="Refresh",width=18,font=("times romans",15,'bold'),foreground='#5449F1',bd=8,command=refresh).place(relx=.28,rely=.75,anchor=CENTER)
    quite_btn=Button(root,text="Quit",width=18,font=("times romans",15,'bold'),foreground='#5449F1',bd=8,command=root.destroy).place(relx=.7,rely=.75,anchor=CENTER)
    
    
    
    root.mainloop()
    
    
    
    
    
if __name__=="__main__":
    account()
