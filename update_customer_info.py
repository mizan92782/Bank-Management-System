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
    acc=Label(root,text="Update Customer Information",font=("lato",40,"bold"),foreground='#5449F1',background='white').place(relx=.5,rely=.05,anchor=CENTER)
   

    
    
  
    
    
    
    
    
    
    ### information------------------------
    
    idl=Label(root,text="Account ID : ",background='#5449F1',foreground='white',font=('times romans',20,'bold')).place(relx=.03,rely=.2)
    id_e=Entry(root,width=30,font=('times romans',15,'bold'))
    id_e.place(relx=.15,rely=.21)
    
    
    number=Label(root,text="Number : ",background='#5449F1',foreground='white',font=('times romans',20,'bold')).place(relx=.03,rely=.3)
    number_e=Entry(root,width=30,font=('times romans',15,'bold'))
    number_e.place(relx=.15,rely=.31)
    
    gmail=Label(root,text="G-mail : ",background='#5449F1',foreground='white',font=('times romans',20,'bold')).place(relx=.03,rely=.4)
    gmail_e=Entry(root,width=30,font=('times romans',15,'bold'))
    gmail_e.place(relx=.15,rely=.41)
    
    password=Label(root,text="Password: ",background='#5449F1',foreground='white',font=('times romans',20,'bold')).place(relx=.03,rely=.5)
    password_e=Entry(root,width=30,font=('times romans',15,'bold'))
    password_e.place(relx=.15,rely=.51)
    
    city=Label(root,text="City : ",background='#5449F1',foreground='white',font=('times romans',20,'bold')).place(relx=.03,rely=.6)
    city_e=Entry(root,width=30,font=('times romans',15,'bold'))
    city_e.place(relx=.15,rely=.61)
  
  
  ## new value -------------------------------
  
  
    Label(root,text="Account ID : ",background='#5449F1',foreground='white',font=('times romans',20,'bold')).place(relx=.5,rely=.2)
    id2_e=Entry(root,width=30,font=('times romans',15,'bold'))
    id2_e.place(relx=.65,rely=.21)
    
    
    number2=Label(root,text="New Number : ",background='#5449F1',foreground='white',font=('times romans',20,'bold')).place(relx=.5,rely=.3)
    number2_e=Entry(root,width=30,font=('times romans',15,'bold'))
    number2_e.place(relx=.65,rely=.31)
    
    gmail2=Label(root,text="New G-mail : ",background='#5449F1',foreground='white',font=('times romans',20,'bold')).place(relx=.5,rely=.4)
    gmail2_e=Entry(root,width=30,font=('times romans',15,'bold'))
    gmail2_e.place(relx=.65,rely=.41)
    
    password2=Label(root,text="New Password: ",background='#5449F1',foreground='white',font=('times romans',20,'bold')).place(relx=.5,rely=.5)
    password2_e=Entry(root,width=30,font=('times romans',15,'bold'))
    password2_e.place(relx=.65,rely=.51)
    
    city2=Label(root,text="New City : ",background='#5449F1',foreground='white',font=('times romans',20,'bold')).place(relx=.5,rely=.6)
    city2_e=Entry(root,width=30,font=('times romans',15,'bold'))
    city2_e.place(relx=.65,rely=.61)
    
    
    
    
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
            query="""select number,gmail,password,city from account where id=%s"""
            cursor.execute(query,(Id,))
            result=cursor.fetchall()
            
            if(len(result)==0):
                MessageBox.showwarning("Invalid Id","No result found,Plz insert correct Id")
                return
            else:
                
                number_e.delete(0,END)
                number_e.insert(END,result[0][0])
                
                gmail_e.delete(0,END)
                gmail_e.insert(END,result[0][1])
                
                password_e.delete(0,END)
                password_e.insert(END,result[0][2])
                
                city_e.delete(0,END)
                city_e.insert(END,result[0][3])
                
                id2_e.delete(0,END)
                id2_e.insert(END,Id)
                
                
            
        
    def update():
        Id=id2_e.get()
        
        if Id=="":
            MessageBox.showwarning("Invalid Id","Fist Search By Id")
            return
        
        Number=number2_e.get()
        if Number=="":
            Number=number_e.get()
            
        Gmail=gmail2_e.get()
        if Gmail=="":
            Gmail=gmail_e.get()
            
        
        Pass=password2_e.get()
        if Pass=="":
            Pass=password_e.get()
        
        
        City=city2_e.get()
        if City=="":
            City=city_e.get()
            
        if Number.isdigit()==False:
            MessageBox.showinfo("Illegat Information","Number contain only digit")
            return
        
        
        cursor=db.cursor()
        query="UPDATE account set number=%s,gmail=%s,password=%s,city=%s where id=%s"
        data=(Number,Gmail,Pass,City,Id)
        cursor.execute(query,data)
        db.commit()
        
        top=Toplevel(root)
        top.title("Information Updated")
        top.geometry("600x700+500+100")
        top.config(background='#5449F1')
        
        Label(top,text=" Thank for update Information \nKeep information securely",background='#5449F1',foreground='white',font=('times romans',25,'bold')).place(relx=.05,rely=.3)
        top.mainloop()
        
        id_e.delete(0,END)
        number_e.delete(0,END)
        gmail_e.delete(0,END)
        password_e.delete(0,END)
        city_e.delete(0,END)
        id2_e.delete(0,END)
        
        
        

        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
    submit_btn=Button(root,text="Submit",width=20,font=("times romans",15,'bold'),foreground='#5449F1',bd=5,command=update).place(relx=.49,rely=.8,anchor=CENTER)
    clear_btn=Button(root,text="Search",width=18,font=("times romans",15,'bold'),foreground='#5449F1',bd=5,command=search).place(relx=.28,rely=.8,anchor=CENTER)
    quite_btn=Button(root,text="Quit",width=18,font=("times romans",15,'bold'),foreground='#5449F1',bd=5,command=root.destroy).place(relx=.7,rely=.8,anchor=CENTER)
    
    
    
    root.mainloop()
    
    
    
    
    
if __name__=="__main__":
    account()
