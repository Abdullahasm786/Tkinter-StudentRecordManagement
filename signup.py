#Importing modules
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql
#FUNCTION

# Function if already have an account 
def login_page():
    signup_window.destroy()
    import login                            # Imports login.py i.e login window

#Function to clear all the entries
def clear():
    emailEntry.delete(0,END)                #0-> start END-> end of string
    usernameEntry.delete(0,END)
    passwordEntry.delete(0,END)
    confirmpasswordEntry.delete(0,END)




#DATABASE CONNECTION
def user_signup():
    if emailEntry.get()=='' or usernameEntry.get()=='' or passwordEntry.get()=='' or confirmpasswordEntry.get()=='':
        messagebox.showerror('Error','All Fields Are Required')
    elif passwordEntry.get() != confirmpasswordEntry.get():
        messagebox.showerror('Error','Password Mismatch')
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='system')         # Creating connection with mysql server
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Database Connectivity Issue Please Try Again A Few Minutes Later')
            return
        # Creating a new database to store all accounts data
        try:
            mycursor.execute('create database userdata')                                    
            mycursor.execute('use userdata')
            mycursor.execute('create table data(id int auto_increment primary key not null,email varchar(50),username varchar(100),password varchar(20))')
        except:
        # If database already exists it'll give an error in previous block and code execution will move into this block where it'll use the previous existing database
            mycursor.execute('use userdata')
        # Checking if username exists so no two accounts exists with same username
        mycursor.execute('select * from data where username=%s',(usernameEntry.get()))
        row=mycursor.fetchone()
        if row !=None:
            messagebox.showerror('Error','Username Already Exists')
        # If username does not already exists then it takes the string from the entry fields to %s in the query and replace it and gets inserted into the database
        else:
            mycursor.execute('insert into data(email,username,password) values(%s,%s,%s)',(emailEntry.get(),usernameEntry.get(),passwordEntry.get()))
            con.commit()                            # commit() is used to update the data or changes in the database 
            con.close()
            messagebox.showinfo('Success','Account Registered Successfully')
            clear()                                 # calls the clear function to clear the entry fields
            signup_window.destroy()                 # destroys the current window
            import login                            # imports login.py window for user to login now using the account they just created
        


#GUI
signup_window=Tk()                                  # TK() creating a window Tk is a class
signup_window.geometry('990x660+150+0')             # dimesions of window the last two values are for where to place the window from x and y ; here it is 150 units on x
signup_window.resizable(False,False)                 
background=ImageTk.PhotoImage(file='bg1.jpg')       # back ground image
bgLabel=Label(signup_window,image=background)       # creating a label placing it on login window with image 

bgLabel.place(x=0,y=0)


frame=Frame(signup_window,bg='white')                # creating a frame in the window with background white
frame.place(x=554,y=100)                             # placing the frame at specific coordinates to suit the image template

heading=Label(frame,text='CREATE AN ACCOUNT',font=('Microsotf Yahei UI Light',18,'bold')    # creating a heading bg= background and fg= foreground i.e font color
              ,bg='white',fg='firebrick1')
heading.grid(row=0,column=0)                        # grid is used to place within the frame so in the frame created earlier we are placing the label 
                                                    # at first row and column and making a distance of 60 units on x axis which moves the text towards right

# Email Label and Entry Box
emailLabel=Label(frame,text='Email',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1') # padx and pady to give spacing from x and y axis
emailLabel.grid(row=1,column=0,sticky='w',padx=25,pady=10)
emailEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='firebrick1')     #Entry create a box to input strings in 
emailEntry.grid(row=2,column=0,sticky='w',padx=25)                                                          # sticky is to keep it towards a direction , w is west it places the object towards the leftmost side of the frame

# Username Label and Entry Box
usernameLabel=Label(frame,text='Username',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
usernameLabel.grid(row=3,column=0,sticky='w',padx=25,pady=10)
usernameEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='firebrick1')
usernameEntry.grid(row=4,column=0,sticky='w',padx=25)
# Passoword Lable and Entry Box
passwordLabel=Label(frame,text='Password',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
passwordLabel.grid(row=5,column=0,sticky='w',padx=25,pady=10)
passwordEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='firebrick1')
passwordEntry.grid(row=6,column=0,sticky='w',padx=25)
# Confirm Passoword Lable and Entry Box
confirmpasswordLabel=Label(frame,text='Confirm Passowrd',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
confirmpasswordLabel.grid(row=7,column=0,sticky='w',padx=25,pady=10)
confirmpasswordEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='firebrick1')
confirmpasswordEntry.grid(row=8,column=0,sticky='w',padx=25)
# Creating a sign up button and assigning a command to it to a function we've defined at the start; bd= border 
signupButton=Button(frame,text='SignUp',font=('Open Sans',16,'bold'),bd=0,bg='firebrick1',fg='white',activebackground='firebrick1',activeforeground='white',width=17,command=user_signup)
signupButton.grid(row=10,column=0,pady=10)
# Already have an account label 
alreadyaccount=Label(frame,text="Already Have An Account?",font=('Open Sans',9,'bold'),bg='white',fg='firebrick1')
alreadyaccount.grid(row=11,column=0,sticky='w',padx=25,pady=10)
# Moving to login window buttion
loginButton=Button(frame,text='log in',font=('Open Sans',9,'bold underline'),bg='white',fg='blue',bd=0,cursor='hand2',activebackground='white',activeforeground='blue'
                 ,command=login_page)
loginButton.grid(row=12,column=0)
# runs the loop regardless of any event until the program is forcefully closed or the user exits the window 
signup_window.mainloop()