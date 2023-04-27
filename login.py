# Importing Modules
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql
# Importing py file
from main import Student

#Functions

# Function for signup button
def signup_page():
    login_window.destroy()
    import signup           # Imports the sign up window {Signup.py}
    
# Function for log in button
def login_user():
    if usernameEntry.get()=='' or passwordEntry.get()=='':  
        messagebox.showerror('Error','All Fields Are Required')
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='system')      # Creating connection with MySQL server
            mycursor=con.cursor()                                                       # Creating a cursor
        except:
            messagebox.showerror('Error','Connection Is Not Established With Database')
            return
        mycursor.execute('use userdata')                                               # Executing a query using the cursor
        mycursor.execute('select * from data where username=%s and password=%s',(usernameEntry.get(),passwordEntry.get()))   #order of %s and .get() inputs the string on the %s spot
        row=mycursor.fetchone()                                                        # fetchone() is used to fetch a single record/row from the table
        if row==None:
            messagebox.showerror('Error','Invalid Username or Password')               # If no record is found that contains the username and password as inputted that means that fetchnone returned None as value which means it found no matching records 
        else:
            messagebox.showinfo('Welcome','Login Sucessful')                           # Else: if it did it'll let show us the login messagebox 
            try:
                con=pymysql.connect(host='localhost',user='root',password='system') # Creating a connection with mysql server
                mycursor=con.cursor()
                mycursor.execute('create database studentdata')
                mycursor.execute('use studentdata')
                # Creating a table for main.py student management if it does not exist
                mycursor.execute('CREATE TABLE data(Student_ID INT NOT NULL,Name VARCHAR(45) NULL,Grade VARCHAR(45) NULL,Division VARCHAR(45) NULL,Year VARCHAR(45) NULL, Course VARCHAR(45) NULL,Gender VARCHAR(45) NULL,Email VARCHAR(45) NULL,Phone_No VARCHAR(45) NULL,Parent_Phone VARCHAR(45) NULL,Parent_Name VARCHAR(45) NULL,Address VARCHAR(45) NULL, DOB VARCHAR(45) NULL,Class_Teacher VARCHAR(45) NULL,PRIMARY KEY (Student_ID))')
                login_window.destroy()                                                 # Destroying the login window         
                Student()                                                              # importing the student class from main file. i.e importing the student management system main window
            except:
                con=pymysql.connect(host='localhost',user='root',password='system')  
                mycursor=con.cursor()
                mycursor.execute('use studentdata')                                    # if the table and database already exists then it'll simply use it and destroy login window and import main
                login_window.destroy()
                Student()
        
# GUI
login_window=Tk()                                       # TK() creating a window Tk is a class
login_window.geometry('990x660+150+0')                  # dimesions of window the last two values are for where to place the window from x and y ; here it is 150 units on x
login_window.resizable(False,False)                     
bgImage=ImageTk.PhotoImage(file='bg.jpg')               # back ground image "photoimage" is a widget for displaying images ,ImageTk module contains support to create and modify Tkinter PhotoImage objects from PIL images. its used wherever we use an image
bgLabel=Label(login_window,image=bgImage)               # creating a label placing it on login window with image 
bgLabel.place(x=0,y=0)                                  # placing the label starting from 0,0 in the window which is the top right corner

frame=Frame(login_window,bg='white')                    # creating a frame in the window with background white
frame.place(x=554,y=100)                                # placing the frame at specific coordinates to suit the image template

heading=Label(frame,text='USER LOGIN',font=('Microsotf Yahei UI Light',18,'bold')       # creating a heading bg= background and fg= foreground i.e font color
              ,bg='white',fg='firebrick1')
heading.grid(row=0,column=0,padx=60)                    # grid is used to place within the frame so in the frame created earlier we are placing the label 
                                                        # at first row and column and making a distance of 60 units on x axis which moves the text towards right

# Username Label and Entry Box
usernamelabel=Label(frame,text='Enter Username',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
usernamelabel.grid(row=1,column=0,sticky='w',padx=25,pady=10)
usernameEntry=Entry(frame,width=30,font=('Microsotf Yahei UI Light',10,'bold'),bg='firebrick1',fg='white')      #Entry create a box to input strings in 
usernameEntry.grid(row=2,column=0,sticky='w',padx=25)   # sticky is to keep it towards a direction , w is west it places the object towards the leftmost side of the frame
# Passoword Lable and Entry Box
passwordlabel=Label(frame,text='Enter Password',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
passwordlabel.grid(row=4,column=0,sticky='w',padx=25,pady=10)
passwordEntry=Entry(frame,width=30,font=('Microsotf Yahei UI Light',10,'bold'),bg='firebrick1',fg='white')
passwordEntry.grid(row=5,column=0,sticky='w',padx=25)



# Creating login button and assigning a command to a functin we've defined at the start of the code
loginButton=Button(frame,text='Login',font=('Open Sans',16,'bold'),bd=0,bg='firebrick1',fg='white',activebackground='firebrick1',activeforeground='white',width=17,command=login_user)
loginButton.grid(row=11,column=0,pady=25,padx=25)
# Label Text
orLabel=Label(frame,text='--------------OR--------------',font=('Open Sans',16),fg='firebrick1',bg='white')
orLabel.grid(row=15,column=0,padx=25,pady=50)
# Create new account label
createnewaccountLabel=Label(frame,text='Don\'t have an account?',font=('Open Sans',9,'bold'),fg='firebrick1',bg='white')
createnewaccountLabel.grid(row=16,column=0,sticky='w',padx=25,pady=10)
# New account buttion 
newaccountButton=Button(frame,text='Create New One',font=('Open Sans',9,'bold underline'),bg='white',fg='blue',bd=0,cursor='hand2',activebackground='white',activeforeground='blue',command=signup_page)
newaccountButton.grid(row=16,column=0,sticky='e',padx=25)
# runs the loop regardless of any event until the program is forcefully closed or the user exits the window 
login_window.mainloop()                 




            
            
                
                                                       
                                                        
                                                        
                                                        
                                                        
                                                       
                                                        
                                                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                           
                                                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                            

                




