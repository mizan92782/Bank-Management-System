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



def main():
    root=Tk()
    root.geometry('600x730+390+20')
    root.title(" Password Retreive!")
    root.config(bg='#5449F1')
    
    def findpassword():
        
        input=inp.get()
        Id=id_e.get()
        email=gmail_e.get()
        
        if(Id=="" or email==""):
            MessageBox.showwarning("Illegal insert", "All Fields are Required")
        elif Id.isdigit()==False:
             MessageBox.showwarning("Illegal insert", "ID id wring format!")
        else:
            
            if input==2:
                
                cursor=db.cursor()
                query="""select gmail,password  from account where id=%s"""
                cursor.execute(query,(Id,))
                result=cursor.fetchall()
                
                
                if(len(result)==0):
                    messagebox.showinfo("Undefinde Id ","Id not found!,plz inter correct id")
                elif(result[0][0]!=email):
                    messagebox.showinfo("Information not match","Plz input Correct information")
                else:
                    
                    pass_e.insert(END,result[0][1])
                    Label(root,text="Keep password,dont share with other",font=("times and romans",17,"bold"),foreground='white',background='#5449F1').place(relx=.1,rely=.8)
            else:
                
                cursor=db.cursor()
                query="""select email,password  from employee where id=%s"""
                cursor.execute(query,(Id,))
                result=cursor.fetchall()
                
                
                if(len(result)==0):
                    messagebox.showinfo("Undefinde Id ","Id not found!,plz inter correct id")
                elif(result[0][0]!=email):
                    messagebox.showinfo("Information not match","Plz input Correct information")
                else:
                    
                    pass_e.insert(END,result[0][1])
                    Label(root,text="Keep password,dont share with other",font=("times and romans",17,"bold"),foreground='white',background='#5449F1').place(relx=.1,rely=.8)
                    
                        
                    
    
    
    
    
    
    
    
    l=Label(root,text="Password Retrieive",font=("times and romans",25,"bold"),foreground='#F9F9FB',background='#5449F1').place(relx=.2,rely=.05)
    id=Label(root,text="Enter ID : ",font=("times and romans",17,"bold"),foreground='#F9F9FB',background='#5449F1').place(relx=.1,rely=.2)
    id_e=Entry(root,width=25,font=("times and romans",14,"bold"),foreground='black',background='white')
    id_e.place(relx=.4,rely=.2)
    
    gmail=Label(root,text="Enter G-mail : ",font=("times and romans",17,"bold"),foreground='#F9F9FB',background='#5449F1').place(relx=.1,rely=.3)
    gmail_e=Entry(root,width=25,font=("times and romans",14,"bold"),foreground='black',background='white')
    gmail_e.place(relx=.4,rely=.3)
    
    
    inp=IntVar(root)
    inp.set(1)
    Radiobutton(root,text="Authority",variable=inp,value=1,background='#5449F1',foreground='black',font=('times romans',15,'bold')).place(relx=.3,rely=.4)
    Radiobutton(root,text="Client",variable=inp,value=2,background='#5449F1',foreground='black',font=('times romans',15,'bold')).place(relx=.53,rely=.4)
    
    Button(root,text='Click',width=10,font=("times romans",15,'bold'),foreground='black',bd=2,command=findpassword).place(relx=.5,rely=.5,anchor=CENTER)


   
    password=Label(root,text="Password : ",font=("times and romans",17,"bold"),foreground='#F9F9FB',background='#5449F1').place(relx=.1,rely=.7)
    pass_e=Entry(root,width=25,font=("times and romans",14,"bold"),foreground='black',background='white')
    pass_e.place(relx=.4,rely=.7)
    
    def login():
        root.destroy()
        call(["python",'login.py'])
        quit()
        
    
    Button(root,text="             Quit             ",font=("times romans",10,'bold'),foreground='black',bd=2,command=login).place(relx=.5,rely=.9,anchor=CENTER)
   
    
    
    
    
    
    root.mainloop()
    



    
if __name__=="__main__":
    main()
    