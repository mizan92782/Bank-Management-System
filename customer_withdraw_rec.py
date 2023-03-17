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
     
    def __init__(self,root,l,m,result):
         
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
                self.e.insert(END, result[i][j])
                self.e.config(relief='sunken')
                



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
                query="""select * from withdraw where id=%s"""
                cursor.execute(query,(Id,))
                 
                result=cursor.fetchall()
               
                
                if(len(result)==0):
                     MessageBox.showinfo("Customer login Security","Unsucesfull attempt! Wrong informatio")
                     return
                
                
                attribut=("ID","CURRENT BALANCE","WITHDRAW AMOUNT","NEW BALANCE","DATE")
                result.insert(0,attribut)
                l=len(result)
                m=len(result[0])
                
                root1=Tk()
                root1.title("DEPOSITE RECORD")
                width = root1.winfo_screenwidth()
                height = root1.winfo_screenheight()
                root1.geometry(f"{width}x{height}")
                root1.config(background='#5050CE')
                
                print(result)

                Table(root1,l,m,result)
                    
                root1.mainloop()

                
                    
               
                
                             
                     
                
            
    
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

    

