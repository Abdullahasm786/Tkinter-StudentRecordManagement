# Importing modules
from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
from PIL import Image,ImageTk
import pymysql


#Creating GUI WINDOW and a CLASS
class Student():
    def __init__(main):
        main.window=Tk()                                 # Creating a window
        main.window.geometry('1128x634+70+0')            # Dimensions of window + placement in the screen
        main.window.title('STUDENT MANAGEMENT SYSTEM')   # Window title
        main.window.resizable(False,False)
        

        background=Image.open('bg4.png')                 # Adding a background image
        main.photoimg_4=ImageTk.PhotoImage(background)
        background_label=Label(main.window,image=main.photoimg_4)   # Making a label and adding the background image
        background_label.place(x=0,y=0)  
        # Title ttext
        title_label=Label(background_label,text="Student Management",font=('Arial',30,'bold underline'),fg='white',bg='#EF4165') 
        title_label.place(x=400,y=0)

        #VARIABLES TO GET THE ENTERED DATA FROMT THE ENTRY FIELDS AND COMBOBOXES IN STRING  StringVar holds an string value
        main.var_grade=StringVar()
        main.var_course=StringVar()
        main.var_year=StringVar()
        main.var_studentid=StringVar()
        main.var_name=StringVar()
        main.var_division=StringVar()
        main.var_gender=StringVar()
        main.var_dob=StringVar()
        main.var_email=StringVar()
        main.var_phone=StringVar()
        main.var_parentname=StringVar()
        main.var_parent_phone=StringVar()
        main.var_address=StringVar()
        main.var_classteacher=StringVar()
        main.var_blank=StringVar()
        







        #MAIN FRAME
        
        frame=Frame(background_label,relief=RIDGE,bg='white')     # Creating a main frame on the window
        frame.place(x=47,y=55,width=1020,height=550)              # relief gives a 3d look to the frame


         

        #CREATING Left Frame [LabelFrame= Frame + Label] 
        LeftFrame=LabelFrame(frame,relief=RIDGE,padx=2,text='Information Input',font=('Arial',12,'bold'),fg='#EF4165',bg='white')  # Creating a frame within the main frame
        LeftFrame.place(x=0,y=0,width=400,height=550)        #Placing the frame within the main frame 



        #Course label
        course_label_frame=LabelFrame(frame,bd=4,relief=SUNKEN,text='Current Course',font=('Arial',9,'bold'),fg='Blue',bg='white')  # Creating a label frame
        course_label_frame.place(x=3,y=20,width=390,height=100)

        
        # CREATING LABELS AND INPUT BOXES.
        #Grade
        grade_label=Label(course_label_frame,text='Grade:',font=('Times New Roman',10,'bold'),fg='BLACK',bg='white') 
        grade_label.grid(row=0,column=0,padx=2,sticky='W') 
        #CREATE COMOBOX TO CHOOSE OPTIONS FROM
        combobox_grade=ttk.Combobox(course_label_frame,textvariable=main.var_grade,font=('Times New Roman',10,'bold'),width=15,state='readonly')    # State makes the state of option in entries box to either be readonly so they can't be edited by user
                                                                                                                                                    # text variable gets the inputted data from the user
        combobox_grade['value']=('Select Grade','1','2','3','4','5','6','7','8','9','10','11','12')   #ENTERING OPTIONS IN COMBOBOX
        combobox_grade.current(0)                                                                     #KEEPS THE OPTION AT VALUE 0 BY DEFAULT I.E "SELECT GRADE" WILL BE DISPLAYED UNLESS A SPECIFIC CHOICE IS CHOOSEN
        combobox_grade.grid(row=0,column=1,padx=2,pady=5)

        # course
        course_label=Label(course_label_frame, font=("arial",10, "bold"),text="Courses:",bg="white")
        course_label.grid(row=0,column=2, sticky='W',pady=5)
        course_combobox=ttk.Combobox(course_label_frame,textvariable=main.var_course,state= 'readonly',font=('Times new roman' ,10, 'bold'),width=17)
        course_combobox["value"]=("Select Course","General","Commerce","Science+Maths", "Science+Biology",'Science+CS','Arts','Humanaties','Psycology')
        course_combobox.current(0)
        course_combobox.grid(row=0, column=3,sticky=W,pady=10)

        #Year/Batch
        year_label=Label(course_label_frame,font=('Times New Roman',10,'bold'),fg='BLACK',bg='white',text='Year:')
        year_label.grid(row=1,column=0,sticky='W',padx=2,pady=5)

        year_combobox=ttk.Combobox(course_label_frame,textvariable=main.var_year,state='readonly',font=('Times New Roman',10,'bold'),width=15)
        year_combobox['value']=('Select Year','2019-2020','2020-2021','2021-2022','2022-2023')
        year_combobox.current(0)
        year_combobox.grid(row=1,column=1,sticky='w',padx=2)


        #CLASS label
        student_info_frame=LabelFrame(frame,bd=4,relief=SUNKEN,text='Student Class Information ',font=('Arial',9,'bold'),fg='Blue',bg='white')
        student_info_frame.place(x=2,y=125,width=390,height=390)

        #Student ID 
        student_id=Label(student_info_frame,font=('Times New Roman',10,'bold'),fg='BLACK',bg='white',text='Student ID:')
        student_id.grid(row=0,column=0,sticky='W',padx=2,pady=3)
        id_entry=ttk.Entry(student_info_frame,textvariable=main.var_studentid,font=('Times New Roman',10,'bold'),width=22) 
        id_entry.grid(row=0,column=1,sticky='w',padx=2,pady=3)

        # Name
        Name_label=Label(student_info_frame,font=('Times New Roman',10,'bold'),text='Student Name :',bg='white')
        Name_label.grid(row=1,column=0,padx=2,pady=7,sticky='w')

        name=ttk.Entry(student_info_frame,textvariable=main.var_name,width=22,font=('Times New Roman',10,'bold'))
        name.grid(row=1,column=1,padx=2,pady=7,sticky='w')

        #Division
        division_label=Label(student_info_frame,font=('Times New Roman',10,'bold'),text='Class Division :',bg='white')
        division_label.grid(row=2,column=0,padx=1,pady=5,sticky='w')
        division_combobox=ttk.Combobox(student_info_frame,textvariable=main.var_division,state='readonly',font=('Times New Roman',10,'bold'),width=22)
        division_combobox['value']=('Select Division','A','B','C')
        division_combobox.current(0)
        division_combobox.grid(row=2,column=1,padx=2,pady=7,sticky='w')

        #Gender
        gender_label=Label(student_info_frame,font=('Times New Roman',10,'bold'),text='Gender :',bg='white')
        gender_label.grid(row=3,column=0,pady=5,sticky='w',padx=2)

        gender_combobox=ttk.Combobox(student_info_frame,textvariable=main.var_gender,state='readonly',font=('Times New Roman',10,'bold'),width=22)
        gender_combobox['value']=('Select Gender','Male','Female')
        gender_combobox.current(0)
        gender_combobox.grid(row=3,column=1,padx=2,pady=2,sticky='w')

        #DOB
        DOB_label=Label(student_info_frame,font=('Times New Roman',10,'bold'),text='DOB :',bg='white')
        DOB_label.grid(row=4,column=0,pady=5,sticky='w',padx=2)
        DOB_entry=ttk.Entry(student_info_frame,textvariable=main.var_dob,width=22,font=('Times New Roman',10,'bold'))
        DOB_entry.insert(0,'DD/MM/YYYY')                                    # displays the text in the box until removed by the user themselves
        DOB_entry.grid(row=4,column=1,padx=2,pady=7,sticky='w')

        #Email
        email_label=Label(student_info_frame,font=('Times New Roman',10,'bold'),text='Email :',bg='white')
        email_label.grid(row=5,column=0,padx=2,pady=5,sticky='w')
        email_entry=ttk.Entry(student_info_frame,textvariable=main.var_email,width=22,font=('Times New Roman',10,'bold'))
        email_entry.grid(row=5,column=1,padx=2,pady=5,sticky='w')

        #Phone Number
        phone_label=Label(student_info_frame,font=('Times New Roman',10,'bold'),text='Phone No.',bg='white')
        phone_label.grid(row=6,column=0,padx=2,pady=5,sticky='w')
        phone_entry=ttk.Entry(student_info_frame,textvariable=main.var_phone,width=22,font=('Times New Roman',10,'bold'))
        phone_entry.grid(row=6,column=1,padx=2,pady=5,sticky='w')

        #Parent Name
        parent_name_label=Label(student_info_frame,font=('Times New Roman',10,'bold'),text='Parent Name :',bg='white')
        parent_name_label.grid(row=7,column=0,padx=2,pady=5,sticky='w')
        parent_name_entry=ttk.Entry(student_info_frame,textvariable=main.var_parentname,width=22,font=('Times New Roman',10,'bold'))
        parent_name_entry.grid(row=7,column=1,padx=2,pady=5,sticky='w')

        #Parent Phone Number

        phone_parent_label=Label(student_info_frame,font=('Times New Roman',10,'bold'),text='Parent Phone No.',bg='white')
        phone_parent_label.grid(row=8,column=0,padx=2,pady=5,sticky='w')
        phone_parent_entry=ttk.Entry(student_info_frame,textvariable=main.var_parent_phone,width=22,font=('Times New Roman',10,'bold'))
        phone_parent_entry.grid(row=8,column=1,padx=2,pady=5,sticky='w')

        #Address
        address_label=Label(student_info_frame,font=('Times New Roman',11,'bold'),text='Address :',bg='white')
        address_label.grid(row=9,column=0,padx=2,pady=5,sticky='w')
        address_entry=ttk.Entry(student_info_frame,textvariable=main.var_address,width=22,font=('Times New Roman',10,'bold'))
        address_entry.grid(row=9,column=1,padx=2,pady=3,sticky='w')
        #Class Teacher
        classteacher_label=Label(student_info_frame,font=('Times New Roman',10,'bold'),text='Class Teacher :',bg='white')
        classteacher_label.grid(row=10,column=0,padx=2,pady=5,sticky='w')
        classteacher_entry=ttk.Entry(student_info_frame,textvariable=main.var_classteacher,width=22,font=('Times New Roman',10,'bold'))
        classteacher_entry.grid(row=10,column=1,padx=2,pady=3,sticky='w')

        #Creating Button Frame

        button_frame=Frame(LeftFrame,bd=2,relief=SUNKEN,bg='white')
        button_frame.place(x=0,y=500,width=500,height=70) 
        #Button specifies its a button and we can add command to it and define the command later on 
        Add_button=Button(button_frame,text='Save',command=main.add_data,font=('Times New Roman',10,'bold'),bg='blue',fg='white',width=13)
        Add_button.grid(row=0,column=0)

        Update_button=Button(button_frame,text='Update',command=main.update_data,font=('Times New Roman',10,'bold'),bg='blue',fg='white',width=12)
        Update_button.grid(row=0,column=1)

        Delete_button=Button(button_frame,text='Delete',command=main.delete_data,font=('Times New Roman',10,'bold'),bg='blue',fg='white',width=13)
        Delete_button.grid(row=0,column=2)

        Reset_button=Button(button_frame,text='Reset',command=main.reset_data,font=('Times New Roman',10,'bold'),bg='blue',fg='white',width=13)
        Reset_button.grid(row=0,column=3)

        


        #Creating Right Frame within the main frame
        RightFrame=LabelFrame(frame,bd=4,relief=RIDGE,padx=2,text='Student Data',font=('Arial',12,'bold'),fg='#EF4165',bg='white')
        RightFrame.place(x=410,y=0,width=605,height=550)
        #Creating Search Label Frame within the right frame
        Search_Frame=LabelFrame(RightFrame,bd=4,relief=SUNKEN,padx=2,text='Search Student Information',font=('Arial',10,'bold'),fg='Blue',bg='white')
        Search_Frame.place(x=0,y=0,width=590,height=55)
        search_by=Label(Search_Frame,font=('Arial',10,'bold'),text='Search By:',bg='white',fg='Black')
        search_by.grid(row=0,column=0,padx=2,pady=5,sticky='w')

        # SEARCHING DATA

        main.var_com_search=StringVar() # variable for combobox
        search_combobox=ttk.Combobox(Search_Frame,textvariable=main.var_com_search,state='readonly',font=('Times New Roman',10,'bold'),width=17)
        search_combobox['value']=('Select Option','Phone_No','Student_ID','Parent_Phone','Name')
        search_combobox.current(0)
        search_combobox.grid(row=0,column=1,sticky='w',padx=2,pady=5)
        main.var_search=StringVar()# variable For entry box
        search_entry=ttk.Entry(Search_Frame,textvariable=main.var_search,width=22,font=('Times new roman',10,'bold'))
        search_entry.grid(row=0,column=2,padx=5)
        #Buttons
        search_button=Button(Search_Frame,command=main.search_data,text='Search',font=('Times New Roman',10,'bold'),bg='blue',fg='white',width=10)
        search_button.grid(row=0,column=3,padx=5)
        ShowAll_button=Button(Search_Frame,command=main.fetch_data,text='Show All',font=('Times New Roman',10,'bold'),bg='blue',fg='white',width=10)
        ShowAll_button.grid(row=0,column=4,padx=5)


        # ===================== Student Table & Scroll Bar====================

        table_frame=Frame(RightFrame,bd=3,relief=RIDGE)        # Creating a table frame within the right frame
        table_frame.place(x=0,y=60,width=590,height=440)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)  #CREATES A SCROLLBAR
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        #TREEVIEW GIVES TABLE VIEW OF THE DATA  
        main.student_table=ttk.Treeview(table_frame,column=('Student_ID','Name','Grade','Division','year','Course','Gender','Email','Phone_No','Parent_Phone','Parent_Name','Address','DOB','Class_Teacher'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X) #PACK WORKS LIKE PLACE; TO PLACE THE SCROLLBAR 
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=main.student_table.xview) #DEFINES THE SHOW MOVEMENT OF SCROLLBAR
        scroll_y.config(command=main.student_table.yview)

        #PUTTING THE TEXT TO BE DISPLAYED ON THE TABLE ON THE RIGHT FRAME WHILE THE VARIABLE IT'LL BE REFERRING IT TO AS IN THE CODE
        main.student_table.heading("Student_ID",text="Student ID")
        main.student_table.heading("Name",text="Name")
        main.student_table.heading("Grade",text="Grade")
        main.student_table.heading("Division",text="Division")
        main.student_table.heading("year",text="Year")
        main.student_table.heading("Course",text="Course")
        main.student_table.heading("Gender",text="Gender")
        main.student_table.heading("Email",text="Email")
        main.student_table.heading("Phone_No",text="Phone No.")
        main.student_table.heading("Parent_Phone",text="Parent Phone")
        main.student_table.heading("Parent_Name",text="Parent Name")
        main.student_table.heading("Address",text="Address")
        main.student_table.heading("DOB",text="DOB")
        main.student_table.heading("Class_Teacher",text="Class Teacher")
        
        #to make all the headings be shifted towards the left so no gap is on left side
        main.student_table['show']='headings'

        #SIZE OF EACH COULUM DISPLAYED
        main.student_table.column("Student_ID",width=100)
        main.student_table.column("Name",width=100)
        main.student_table.column("Grade",width=100)
        main.student_table.column("Division",width=100)
        main.student_table.column("year",width=100)
        main.student_table.column("Course",width=100)
        main.student_table.column("Gender",width=100)
        main.student_table.column("Email",width=100)
        main.student_table.column("Phone_No",width=100)
        main.student_table.column("Parent_Phone",width=100)
        main.student_table.column("Parent_Name",width=100)
        main.student_table.column("Address",width=100)
        main.student_table.column("DOB",width=100)
        main.student_table.column("Class_Teacher",width=100)
        #TO DISPLAY THE HEADINGS 
        main.student_table.pack(fill=BOTH,expand=1)

        #Upon clicking a record the data to be inserted in the entry boxes in left frame
        main.student_table.bind('<ButtonRelease>',main.get_cursor)
        # calling function to keep refreshing the table 
        main.fetch_data()


    #ADD BUTTON <MYSQL PART>
    def add_data(main):
        if main.var_course.get()=='' or main.var_year.get()=='' or main.var_studentid.get()=='' or main.var_name.get()=='' or main.var_division.get()=='' or main.var_gender.get()=='' or main.var_dob.get()=='' or main.var_email.get()=='' or main.var_phone.get()=='' or main.var_parent_phone.get()=='' or main.var_address.get()=='' or main.var_classteacher.get()=='' or main.var_parentname.get()=='' :
            messagebox.showerror('Error','All Fields Are Required')
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='system')       #Connection to database and database name to be used
                mycursor=con.cursor()
                #comparing values and get() function to add values into query
                #write the .get() in order of the table made or else the data will be messed up in wrong columns
                mycursor.execute('use studentdata')
                mycursor.execute('insert into data values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(main.var_studentid.get(),main.var_name.get(),main.var_grade.get(),main.var_division.get(),main.var_year.get(),main.var_course.get(),main.var_gender.get(),main.var_email.get(),main.var_phone.get(),main.var_parent_phone.get(),main.var_parentname.get(),main.var_address.get(),main.var_dob.get(),main.var_classteacher.get()))
                con.commit()
                main.fetch_data()                       # Calling the function to refresh the table for newly added data
                con.close()
                messagebox.showinfo('Success','Student Added Successfully',parent=main.window)     # using parent to display the messagebox on top of this main window
            
            except Exception as es:
                messagebox.showerror('Error',f'Action was unsucessfull due to:{str(es)}',parent=main.window)     # using this code to show what kind of error we are getting along with error code
    #data fetch function
    def fetch_data(main):
        con=pymysql.connect(host='localhost',user='root',password='system')
        mycursor=con.cursor()
        mycursor.execute('use studentdata ')
        mycursor.execute('Select * from data')   
        data=mycursor.fetchall()
        if len(data)!=0:
            main.student_table.delete(*main.student_table.get_children())   
            for i in data:
                main.student_table.insert('',END,values=i) 
            con.commit()
        con.close()

    #GET CURSOR to fill the data on left frame entry boxes upon clicking a record in the table
    def get_cursor(main,event=''):
        cursor_row=main.student_table.focus()
        content=main.student_table.item(cursor_row)
        data=content['values']
        main.var_studentid.set(data[0])
        main.var_name.set(data[1])
        main.var_grade.set(data[2])
        main.var_division.set(data[3])
        main.var_year.set(data[4])
        main.var_course.set(data[5])
        main.var_gender.set(data[6])
        main.var_email.set(data[7])
        main.var_phone.set(data[8])
        main.var_parent_phone.set(data[9])
        main.var_parentname.set(data[10])
        main.var_address.set(data[11])
        main.var_dob.set(data[12])
        main.var_classteacher.set(data[13])
        
        
        
        
        

    #UPDATE FUNCTION
    def update_data(main):
        if main.var_course.get()=='' or main.var_year.get()=='' or main.var_studentid.get()=='' or main.var_name.get()=='' or main.var_division.get()=='' or main.var_gender.get()=='' or main.var_dob.get()=='' or main.var_email.get()=='' or main.var_phone.get()=='' or main.var_parent_phone.get()=='' or main.var_address.get()=='' or main.var_classteacher.get()=='' or main.var_parentname.get()=='' :
            messagebox.showerror('Error','All Fields Are Required')
        else:
            try:
                update=messagebox.askyesno('Update','Are you sure you want to update this student data',parent=main.window)
                if update>0:
                     con=pymysql.connect(host='localhost',user='root',password='system')
                     mycursor=con.cursor()
                     mycursor.execute('use studentdata')
                     mycursor.execute('update data set Name=%s,Grade=%s,Division=%s,year=%s,Course=%s,Gender=%s,Email=%s,Phone_No=%s,Parent_Phone=%s,Parent_Name=%s,Address=%s,DOB=%s,Class_Teacher=%s where Student_ID=%s',(       main.var_name.get(),
                                                                                                                                                                                                                                    main.var_grade.get(),
                                                                                                                                                                                                                                    main.var_division.get(),
                                                                                                                                                                                                                                    main.var_year.get(),
                                                                                                                                                                                                                                    main.var_course.get(),
                                                                                                                                                                                                                                    main.var_gender.get(),
                                                                                                                                                                                                                                    main.var_email.get(),
                                                                                                                                                                                                                                    main.var_phone.get(),
                                                                                                                                                                                                                                    main.var_parent_phone.get(),
                                                                                                                                                                                                                                    main.var_parentname.get(),
                                                                                                                                                                                                                                    main.var_address.get(),
                                                                                                                                                                                                                                    main.var_dob.get(),
                                                                                                                                                                                                                                    main.var_classteacher.get(),
                                                                                                                                                                                                                                    main.var_studentid.get()))   
                else: 
                    if not update:
                        return
                con.commit()
                main.fetch_data()
                con.close()
                messagebox.showinfo('Success','Data updated sucessfully',parent=main.window)  

            except Exception as es:
                messagebox.showerror('Error',f'Action was unsucessfull due to:{str(es)}',parent=main.window)

    #DELETE FUNCTION
    def delete_data(main):
        try:
            Delete=messagebox.askyesno('Delete',"Are you sure to delete this student?")
            if Delete>0:
                con=pymysql.connect(host='localhost',user='root',password='system')
                mycursor=con.cursor()
                mycursor.execute('use studentdata')
                mycursor.execute('delete from data where Student_ID=%s',(main.var_studentid.get()))
            else:
                if not Delete:
                    return
            con.commit()
            main.fetch_data()
            con.close()
            messagebox.showinfo('Deleted',"The selected Data has been deleted",parent=main.window)
        except Exception as es:
                messagebox.showerror('Error',f'Action was unsucessfull due to:{str(es)}',parent=main.window)
        main.fetch_data()
    #RESET FUNTION
    def reset_data(main):   
        main.var_studentid.set(" ")
        main.var_name.set(" ")
        main.var_grade.set("Select Grade")
        main.var_division.set("Select Division")
        main.var_year.set("Select Year")
        main.var_course.set("Select Course")
        main.var_gender.set("Select Gender")
        main.var_email.set(" ")
        main.var_phone.set(" ")
        main.var_parent_phone.set(" ")
        main.var_parentname.set(" ")
        main.var_address.set(" ")
        main.var_dob.set(" ")
        main.var_classteacher.set(" ")
    #search data function
    def search_data(main):
        if main.var_com_search.get()=='' or main.var_search.get()=='':
            messagebox.showerror("Error","Please Select Option")
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='system')
                mycursor=con.cursor()
                mycursor.execute('use studentdata')
                mycursor.execute("select * from data where "+str(main.var_com_search.get())+" LIKE '%"+str(main.var_search.get())+"%'")
                data=mycursor.fetchall()
                if len(data)!=0:
                    main.student_table.delete(*main.student_table.get_children())
                    for i in data:
                        main.student_table.insert("",END,values=i)
                    con.commit()
                con.close()
            except Exception as es:
                
                
                
                
                messagebox.showerror('Error',f'Action was unsucessfull due to:{str(es)}',parent=main.window)

if __name__== "__main__":
    Student().window.mainloop()      



        


                                                                                                                                                                                          

                                                                                                                                                                                            
                                                                                                                                                                                            

        

                
            
            
            
                
                


            

        
            
            


       
                                                                                                                                                                                                            

   
    