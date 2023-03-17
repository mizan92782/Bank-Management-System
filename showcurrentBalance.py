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





def search():
    root=Tk()
    
    
    
    root.attributes('-fullscreen', True)
   
   
     
    #design-------------------------------------------------------------------
    
    
        
             
    
    
    
    
    
    
    def widthdraw():
        
        
        
       
        Id=e_id.get()
        Email=e_gmail.get()
        Password=e_pass.get()
        
        if(Id=="" or Email=="" or Password=="" ):
            MessageBox.showwarning("Warning", " All field are required !",)
            return
        elif(Id.isdigit()==False):
                MessageBox.showinfo("Illegal insert", "  Sorry ! inserted wrong format Id ")
                return
        else:   
            
                cursor=db.cursor()
                cursor.execute("SELECT MIN(id),MAX(id) from account")
                account_id=cursor.fetchone()
                
                x=int(account_id[0])
                y=int(account_id[1])
                
                
            
                if(int(Id)<x or int(Id)>y):
                    MessageBox.showinfo("Illegal insert", "Sorry ! Can't find Acount")
                    return
                
                
                query="""select gmail,password from account where id=%s"""
                cursor.execute(query,(Id,))
                 
                result=cursor.fetchall()
                dresult=result[0]
               
                
                
                if(  dresult[0]!=Email or dresult[1]!=Password ):
                     MessageBox.showinfo("Customer login Security","Unsucesfull attempt! Wrong information")
                     return
                else:
                    cursor=db.cursor()
                    query="""select id,first_name,last_name,nid,number,gmail,city,gender,balance from account where id=%s"""
                    cursor.execute(query,(Id,))
                    
                    result=cursor.fetchall()
                    attribute=["ID : ","First Name : ","Last Name : ","NID : ","Number : ","Gmail : ","City : ","Gender : ","Current Balance : "]
                    
                        
                    
                    
                    if(len(result)==0):
                        top=Toplevel(root)
                        top.geometry('600x730+390+20')
                        top.title(" Balance information!")
                        top.config(bg='#5449F1')
                        
                        
                        lone=Label(top,text="No people'Id match with this Id!\nPlz insert wright id.",font=("lato",20,"bold"),foreground='#F9F9FB',background='#5449F1')
                        ltwo=Label(top,text="Wrong Id",font=("times and romans",40,"bold"),foreground='#F9F9FB',background='#5449F1')
                        lone.place(relx=.1,rely=.3)
                        ltwo.place(relx=.2,rely=.1)
                        top.mainloop()
                            
                        
                    else:
                        top=Toplevel(root)
                        top.geometry('600x730+390+20')
                        top.title(" Searching result!")
                        top.config(bg='#5449F1')
                        
                        dresult=result[0]
                        Label(top,text="Customer Information",font=("times and romans",25,"bold"),foreground='#F9F9FB',background='#5449F1').place(relx=.2,rely=.1)
                        
                        Label(top,text=attribute[0],font=("times and romans",15,"bold"),foreground='#F9F9FB',background='#5449F1').place(relx=.2,rely=.3)
                        Label(top,text=dresult[0],font=("times and romans",15,"bold"),foreground='#F9F9FB',background='#5449F1').place(relx=.4,rely=.3)
                        
                        Label(top,text=attribute[1],font=("times and romans",15,"bold"),foreground='#F9F9FB',background='#5449F1').place(relx=.2,rely=.35)
                        Label(top,text=dresult[1],font=("times and romans",15,"bold"),foreground='#F9F9FB',background='#5449F1').place(relx=.4,rely=.35)
                        
                        Label(top,text=attribute[2],font=("times and romans",15,"bold"),foreground='#F9F9FB',background='#5449F1').place(relx=.2,rely=.4)
                        Label(top,text=dresult[2],font=("times and romans",15,"bold"),foreground='#F9F9FB',background='#5449F1').place(relx=.4,rely=.4)
                        
                        Label(top,text=attribute[3],font=("times and romans",15,"bold"),foreground='#F9F9FB',background='#5449F1').place(relx=.2,rely=.45)
                        Label(top,text=dresult[3],font=("times and romans",15,"bold"),foreground='#F9F9FB',background='#5449F1').place(relx=.4,rely=.45)
                        
                        Label(top,text=attribute[4],font=("times and romans",15,"bold"),foreground='#F9F9FB',background='#5449F1').place(relx=.2,rely=.5)
                        Label(top,text=dresult[4],font=("times and romans",15,"bold"),foreground='#F9F9FB',background='#5449F1').place(relx=.4,rely=.5)
                        
                        Label(top,text=attribute[5],font=("times and romans",15,"bold"),foreground='#F9F9FB',background='#5449F1').place(relx=.2,rely=.55)
                        Label(top,text=dresult[5],font=("times and romans",15,"bold"),foreground='#F9F9FB',background='#5449F1').place(relx=.4,rely=.55)
                        
                        
                        Label(top,text=attribute[6],font=("times and romans",15,"bold"),foreground='#F9F9FB',background='#5449F1').place(relx=.2,rely=.6)
                        Label(top,text=dresult[6],font=("times and romans",15,"bold"),foreground='#F9F9FB',background='#5449F1').place(relx=.4,rely=.6)
                        
                        
                        Label(top,text=attribute[7],font=("times and romans",15,"bold"),foreground='#F9F9FB',background='#5449F1').place(relx=.2,rely=.65)
                        Label(top,text=dresult[7],font=("times and romans",15,"bold"),foreground='#F9F9FB',background='#5449F1').place(relx=.4,rely=.65)
                        
                        
                        
                        Label(top,text=attribute[8],font=("times and romans",20,"bold"),foreground='#F9F9FB',background='#5449F1').place(relx=.1,rely=.8)
                        Label(top,text=str(dresult[8])+" TK" ,font=("times and romans",20,"bold"),foreground='#F9F9FB',background='#5449F1').place(relx=.6,rely=.8)
                        
                
                
                        
                        
                        
                        
                        
                
                        
                        
                        
                    
    
                     
                     
                   
                     
                      
                     
                     
                                       
                     
                
            
    
    fone=Frame(root,height=100,bg="white").pack(fill=X)
    ftwo=Frame(root,height=600,bg='#5449F1').pack(fill=X)



    #label

    lone=Label(root,text="Balance Information",font=("lato",40,"bold"),foreground='#5449F1',background='white').place(relx=.5,rely=.05,anchor=CENTER)  



    id=Label(root,text='Enter ID : ',foreground='white',background='#5449F1',font=('times romans',15,'bold')).place(relx=.3,rely=.3)
    e_id=Entry(root,width=40,font=('times romans',12,'bold'))
    e_id.place(relx=.45,rely=.3)
    
    gmail=Label(root,text='Enter G-mail: ',foreground='white',background='#5449F1',font=('times romans',15,'bold')).place(relx=.3,rely=.4)
    e_gmail=Entry(root,width=40,font=('times romans',12,'bold'))
    e_gmail.place(relx=.45,rely=.4)
    
    id=Label(root,text='Enter Password : ',foreground='white',background='#5449F1',font=('times romans',15,'bold')).place(relx=.3,rely=.5)
    e_pass=Entry(root,width=40,font=('times romans',12,'bold'))
    e_pass.place(relx=.45,rely=.5)
    
    
    
    
    serch_btn=Button(root,text="Search",width=15,foreground='#5449F1',background='#F7F7F9',font=('times romans',15,'bold'),command=widthdraw).place(relx=.4,rely=.6)
    Button(root,text="Quit",width=15,foreground='#5449F1',background='#F7F7F9',font=('times romans',15,'bold'),command=root.destroy).place(relx=.6,rely=.6)
    

     
    root.mainloop()
    
    
    
    
    
    
if __name__=="__main__":
    search()

    

