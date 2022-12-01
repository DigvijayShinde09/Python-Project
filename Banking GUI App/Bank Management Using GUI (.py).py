# Imports
from tkinter import *
import os
from PIL import ImageTk, Image
# Main Screen
master = Tk()
master.title("Banking App")

# Functions

# Registering New User -
def register():
    # Variables
    global temp_name
    global temp_age
    global temp_gender
    global temp_password
    global notif
    temp_name = StringVar()
    temp_age = StringVar()
    temp_gender = StringVar()
    temp_password = StringVar() 
    # Register Window
    register_screen = Toplevel(master)
    register_screen.title("Register")
    # Labels
    l1 = Label(register_screen, text="Please enter your details below to register", font=('Times',14))
    l1.grid(row=0,sticky=N,pady=10)   
    l2 = Label(register_screen, text="Name", font=('Calibri',12))
    l2.grid(row=1,sticky=W)   
    l3 = Label(register_screen, text="Age", font=('Calibri',12))
    l3.grid(row=2,sticky=W)   
    l4 = Label(register_screen, text="Gender", font=('Calibri',12))
    l4.grid(row=3,sticky=W)   
    l4 = Label(register_screen, text="Password", font=('Calibri',12))
    l4.grid(row=4,sticky=W) 
    notif = Label(register_screen, font=('Calibri',12))
    notif.grid(row=6,sticky=N,pady=10) 
    # Entries
    e1 = Entry(register_screen,textvariable=temp_name)
    e1.grid(row=1,column=0)
    e2 = Entry(register_screen,textvariable=temp_age)
    e2.grid(row=2,column=0)
    e3 = Entry(register_screen,textvariable=temp_gender)
    e3.grid(row=3,column=0)
    e4 = Entry(register_screen,textvariable=temp_password,show="*")
    e4.grid(row=4,column=0)    
    # Buttons
    b1 = Button(register_screen,text="Register", font=('Calibri',14), width=20, command=finish_reg) 
    b1.grid(row=5,sticky=N,pady=10)

# Finishing Registration -
def finish_reg():
    name = temp_name.get()
    age = temp_age.get()
    gender = temp_gender.get()
    password = temp_password.get()
    all_accounts = os.listdir()
    
    if  name == "" or age == "" or gender == "" or password == "":
        notif.config(fg="red", text="All fiends are Required *")
        return
    # Checkng name with Duplicate entries
    for name_check in all_accounts:
        if name == name_check:
            notif.config(fg="red", text="Account already exists")
            return
        else:
            new_file = open(name,"w")
            new_file.write(name + '\n')
            new_file.write(password + '\n')
            new_file.write(age + '\n')
            new_file.write(gender + '\n')
            new_file.write('0')
            new_file.close()
            notif.config(fg="green", text="Account has been created")

# User's Account Dashboard Window - 
def login_session():
    global login_name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
    all_accounts = os.listdir()
    login_name = temp_login_name.get()
    login_password = temp_login_password.get()    
    for name in all_accounts:
        if name == login_name:
            file = open(name,"r")
            file_data = file.read()
            file_data = file_data.split('\n')
            password = file_data[1] 
            # Account Dashboard
            if login_password == password:
                login_screen.destroy()
                account_dashboard = Toplevel(master)
                account_dashboard.title("Dashboard")
                # labels
                l1 = Label(account_dashboard, text="Account Dashboard", font=('Times',16))
                l1.grid(row=0,sticky=N,pady=10) 
                l2 = Label(account_dashboard, text="Welcome " +name, font=('Times',12))
                l2.grid(row=1,sticky=N,pady=5)
                # Buttons
                b1 = Button(account_dashboard,text="Personal Details", font=('Calibri',14), width=20, command=personal_details) 
                b1.grid(row=2,sticky=N,pady=5)
                b2 = Button(account_dashboard,text="Deposit", font=('Calibri',14), width=20, command=deposit) 
                b2.grid(row=3,sticky=N,pady=5)
                b3 = Button(account_dashboard,text="Withdraw", font=('Calibri',14), width=20, command=withdraw) 
                b3.grid(row=4,sticky=N,pady=5)
                
                return
            else:
                login_notif.config(fg="red", text="Incorrect Password!")   
                return
    login_notif.config(fg="red", text="No such Account found!")  

# Deposit Window -
def deposit():
    # Vars
    global amount
    global deposit_notif
    global current_balance_label
    amount = StringVar()
    file = open(login_name,"r")
    file_data = file.read()
    user_details = file_data.split('\n')
    details_balance = user_details[4]
    # Deposit Screen
    deposit_screen = Toplevel(master)
    deposit_screen.title("Deposit")
    # labels
    l1 = Label(deposit_screen, text="Deposit Amount", font=('Times',16))
    l1.grid(row=0,sticky=N,pady=10) 
    current_balance_label = Label(deposit_screen, text="Current Balance : $"+details_balance, font=('Calibri',12))
    current_balance_label.grid(row=1,sticky=W)
    l2 = Label(deposit_screen, text="Amount : ", font=('Calibri',12))
    l2.grid(row=2,sticky=W) 
    deposit_notif = Label(deposit_screen, font=('Calibri',12))
    deposit_notif.grid(row=4,sticky=N,pady=5) 
    # Entry
    e1 = Entry(deposit_screen,textvariable=amount)
    e1.grid(row=2,column=1)
    # Button
    b1 = Button(deposit_screen,text="Finish", font=('Calibri',14), width=20, command=finish_deposit) 
    b1.grid(row=3,sticky=W,pady=5,padx=5)
    
def finish_deposit():
    if amount.get() == "":
        deposit_notif.config(fg='red', text="Please Enter Amount")
        return
    if float(amount.get()) <= 0:
        deposit_notif.config(fg='red', text="Negative amount can't accepted")
        return
    
    file = open(login_name,"r+")
    file_data = file.read()
    details = file_data.split('\n')
    current_balance = details[4]
    updated_balance = current_balance
    updated_balance = round(float(updated_balance) + float(amount.get()),2)
    file_data = file_data.replace(current_balance, str(updated_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()
    
    current_balance_label.config(fg='green', text="Current Balance : $" +str(updated_balance))
    deposit_notif.config(fg='green', text="Balance has been Updated")

# Withdraw Window -
def withdraw():
    # Vars
    global withdraw_amount
    global withdraw_notif
    global current_balance_label
    withdraw_amount = StringVar()
    file = open(login_name,"r")
    file_data = file.read()
    user_details = file_data.split('\n')
    details_balance = user_details[4]
    # Deposit Screen
    withdraw_screen = Toplevel(master)
    withdraw_screen.title("Withdraw")
    # labels
    l1 = Label(withdraw_screen, text="Withdraw Amount", font=('Times',16))
    l1.grid(row=0,sticky=N,pady=10) 
    current_balance_label = Label(withdraw_screen, text="Current Balance : $" +details_balance, font=('Calibri',12))
    current_balance_label.grid(row=1,sticky=W)
    l2 = Label(withdraw_screen, text="Amount : ", font=('Calibri',12))
    l2.grid(row=2,sticky=W) 
    withdraw_notif = Label(withdraw_screen, font=('Calibri',12))
    withdraw_notif.grid(row=4,sticky=N,pady=5) 
    # Entry
    e1 = Entry(withdraw_screen,textvariable=withdraw_amount)
    e1.grid(row=2,column=1)
    # Button
    b1 = Button(withdraw_screen,text="Finish", font=('Calibri',14), width=20, command=finish_withdraw) 
    b1.grid(row=3,sticky=W,pady=5,padx=5)
    
def finish_withdraw():
    if withdraw_amount.get() == "":
        withdraw_notif.config(fg='red', text="Please Enter Amount")
        return
    if float(withdraw_amount.get()) <= 0:
        withdraw_notif.config(fg='red', text="Negative amount can't accepted")
        return
    
    file = open(login_name,"r+")
    file_data = file.read()
    details = file_data.split('\n')
    current_balance = details[4]
    
    if float(withdraw_amount.get()) > float(current_balance):
        withdraw_notif.config(fg='red', text="Insufficient Funds!")
        return
    
    updated_balance = current_balance
    updated_balance = round(float(updated_balance) - float(withdraw_amount.get()),2)
    file_data = file_data.replace(current_balance, str(updated_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()
    
    current_balance_label.config(fg='green', text="Current Balance : $" +str(updated_balance))
    withdraw_notif.config(fg='green', text="Balance has been Updated")

# Personal Details Window - 
def personal_details():
    # Vars
    file = open(login_name,"r")
    file_data = file.read()
    user_details = file_data.split('\n')
    details_name = user_details[0]
    details_age = user_details[2]
    details_gender = user_details[3]
    details_balance = user_details[4]
    #  Personal Details Screen
    personal_details_screen = Toplevel(master)
    personal_details_screen.title("Personal Details")
    # labels
    l1 = Label(personal_details_screen, text="Personal Details", font=('Times',16))
    l1.grid(row=0,sticky=N,pady=10) 
    l2 = Label(personal_details_screen, text="Name : " +details_name, font=('Times',12))
    l2.grid(row=1,sticky=W)
    l3 = Label(personal_details_screen, text="Age : " +details_age, font=('Times',12))
    l3.grid(row=2,sticky=W)
    l4 = Label(personal_details_screen, text="Gender : " +details_gender, font=('Times',12))
    l4.grid(row=3,sticky=W)
    l5 = Label(personal_details_screen, text="Balance : $ " +details_balance, font=('Times',12))
    l5.grid(row=4,sticky=W)

# Login Window -
def login():
    # Variables
    global temp_login_name
    global temp_login_password
    global login_notif
    global login_screen
    temp_login_name = StringVar()
    temp_login_password = StringVar()   
    # Login Screen
    login_screen = Toplevel(master)
    login_screen.title("Login")    
    # Labels
    l1 = Label(login_screen, text="Login to Your Account",font=('Times',14))
    l1.grid(row=0,sticky=N,pady=10)
    l2 = Label(login_screen, text="Username",font=('Calibri',12))
    l2.grid(row=1,sticky=W)
    l3 = Label(login_screen, text="Password",font=('Calibri',12))
    l3.grid(row=2,sticky=W)
    login_notif = Label(login_screen, font=('Calibri',12))
    login_notif.grid(row=4,sticky=N)    
    # Entries
    e1 = Entry(login_screen,textvariable=temp_login_name)
    e1.grid(row=1,column=1,padx=5)
    e1 = Entry(login_screen,textvariable=temp_login_password,show="*")
    e1.grid(row=2,column=1,padx=5)    
    # Buttons
    b1 = Button(login_screen,text="Login", font=('Calibri',14), width=20, command=login_session) 
    b1.grid(row=3,sticky=W,pady=5,padx=5)


# Main Screen Editing -
# Import Image
img = Image.open('secure.png')
img = img.resize ((150,150))
img = ImageTk.PhotoImage(img)
# Labels 
l1 = Label(master,text="Mobile Banking", font=('Times',14))
l1.grid(row=0,sticky=N,pady=10)
i1 = Label(master, image=img)
i1.grid(row=2,sticky=N,pady=15)
# Button
b1 = Button(master,text="Register", font=('Calibri',14), width=20, command=register ) 
b1.grid(row=3,sticky=N)
b2 = Button(master,text="Login", font=('Calibri',14), width=20, command=login) 
b2.grid(row=4,sticky=N,pady=10)
master.mainloop()



