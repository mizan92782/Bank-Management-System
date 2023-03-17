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
    
    def check():
        
        inp=people.get()
        Id=e_id.get()
        
        if(Id==""):
            
            MessageBox.showinfo("Warning", "          Id is Empty       ",)
            return
        elif(Id.isdigit()==False):
                MessageBox.showinfo("Illegal insert", "  Sorry ! inserted wrong format Id ")
                return
        else:
             if(inp==2):
                 cursor=db.cursor()
                 query="""select id,first_name,last_name,nid,number,gmail,city,gender,date,balance from account where id=%s"""
                 cursor.execute(query,(Id,))
                 
                 result=cursor.fetchall()
                 attribute=["ID : ","First Name : ","Last Name : ","NID : ","Number : ","Gmail : ","City : ","Gender : ","A/C Date : ","Balance : "]
                
                    
                 
                 
                 if(len(result)==0):
                     top=Toplevel(root)
                     top.geometry('600x730+390+20')
                     top.title(" Searching result!")
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
                     
                     
                     
                     Label(top,text=attribute[8],font=("times and romans",15,"bold"),foreground='#F9F9FB',background='#5449F1').place(relx=.2,rely=.7)
                     Label(top,text=dresult[8],font=("times and romans",15,"bold"),foreground='#F9F9FB',background='#5449F1').place(relx=.4,rely=.7)
                     
                     
                     Label(top,text=attribute[9],font=("times and romans",15,"bold"),foreground='#F9F9FB',background='#5449F1').place(relx=.2,rely=.75)
                     Label(top,text=str(dresult[9])+" TK ",font=("times and romans",15,"bold"),foreground='#F9F9FB',background='#5449F1').place(relx=.4,rely=.75)
                     
             else:
                 cursor=db.cursor()
                 query="""select id,first_name,last_name,nid,number,email,city,gender,joindata,salary,status from employee where id=%s"""
                 cursor.execute(query,(Id,))
                 
                 result=cursor.fetchall()
                 attribute=["ID : ","First Name : ","Last Name : ","NID : ","Number : ","Gmail : ","City : ","Gender : ","Join-Date: ","Salary : ","Status : "]
                
                    
                 
                 
                 if(len(result)==0):
                     top=Toplevel(root)
                     top.geometry('600x730+390+20')
                     top.title(" Searching result!")
                     top.config(bg='#5449F1')
                     
                     
                     lone=Label(top,text="No Employee'Id match with this Id!\nPlz insert wright id.",font=("lato",20,"bold"),foreground='#F9F9FB',background='#5449F1')
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
                     Label(top,text="Employee Information",font=("times and romans",25,"bold"),foreground='#F9F9FB',background='#5449F1').place(relx=.2,rely=.1)
                     
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
                     
                     Label(top,text=attribute[8],font=("times and romans",15,"bold"),foreground='#F9F9FB',background='#5449F1').place(relx=.2,rely=.7)
                     Label(top,text=dresult[8],font=("times and romans",15,"bold"),foreground='#F9F9FB',background='#5449F1').place(relx=.4,rely=.7)
                     
                     Label(top,text=attribute[9],font=("times and romans",15,"bold"),foreground='#F9F9FB',background='#5449F1').place(relx=.2,rely=.75)
                     Label(top,text=str(dresult[9])+" TK",font=("times and romans",15,"bold"),foreground='#F9F9FB',background='#5449F1').place(relx=.4,rely=.75)
                     
                     Label(top,text=attribute[10],font=("times and romans",15,"bold"),foreground='#F9F9FB',background='#5449F1').place(relx=.2,rely=.8)
                     Label(top,text=dresult[10],font=("times and romans",15,"bold"),foreground='#F9F9FB',background='#5449F1').place(relx=.4,rely=.8)
                     
                     Label(top,text=attribute[11],font=("times and romans",15,"bold"),foreground='#F9F9FB',background='#5449F1').place(relx=.2,rely=.85)
                     Label(top,text=dresult[11],font=("times and romans",15,"bold"),foreground='#F9F9FB',background='#5449F1').place(relx=.4,rely=.85)
                     
                     
                     
                    
                     
                     
                     
                    
                     
                     
                     
                    
                     
                     
                     
                    
                     
                     
                     
                    
               
                     
                     
                     
                     
                     
                     
                     
                      
                     
                     
                        
                        
                    
                     
                
                
                
                      
                      
                     
                
            
    
    fone=Frame(root,height=100,bg="white").pack(fill=X)
    ftwo=Frame(root,height=600,bg='#5449F1').pack(fill=X)



    #label

    lone=Label(root,text="Search People",font=("lato",40,"bold"),foreground='#5449F1',background='white').place(relx=.5,rely=.05,anchor=CENTER)  

    id=Label(root,text='Enter ID : ',foreground='white',background='#5449F1',font=('times romans',15,'bold')).place(relx=.3,rely=.3)
    e_id=Entry(root,width=40,font=('times romans',12,'bold'))
    e_id.place(relx=.4,rely=.3)
    
    people=IntVar()
    people.set(1)
    Radiobutton(root,text="Authority",variable=people,value=1,background='#5449F1',foreground='black',font=('times romans',20,'bold')).place(relx=.4,rely=.4)
    Radiobutton(root,text="Client",variable=people,value=2,background='#5449F1',foreground='black',font=('times romans',20,'bold')).place(relx=.55,rely=.4)

    
    
    serch_btn=Button(root,text="Search",width=15,foreground='#5449F1',background='#F7F7F9',font=('times romans',15,'bold'),command=check).place(relx=.45,rely=.5)
    Quit=Button(root,text="Quit",width=30,foreground='#5449F1',background='#F7F7F9',font=('times romans',15,'bold'),command=root.destroy).place(relx=.4,rely=.7)
    

     
    root.mainloop()
    
    
    
    
    
    
if __name__=="__main__":
    search()

    

