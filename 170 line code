import tkinter as tk

logindaten = {"admin":"123"}
usernames = logindaten.keys()
usernamesinalist = list(usernames)

def registration_clearusernameentry(event):
    global  registration_enteredusername
    registration_enteredusername = registration_usernameentry.get()

    if registration_enteredusername == "username":
        registration_usernameentry.delete(0,"end")
    registration_usernameentry.config(fg='black')
def registration_clearpasswordentry(event):
    global registration_enteredpassword
    registration_enteredpassword = registration_passwordentry.get()

    if registration_enteredpassword == "password":
        registration_passwordentry.delete(0,"end")
    registration_passwordentry.config(fg='black')

def newaccount():
    registration_enteredusername = registration_usernameentry.get()
    registration_enteredpassword = registration_passwordentry.get()
    usernames = logindaten.keys()
    usernamesinalist = list(usernames)

    uit = None
    #print(registration_enteredusername, registration_enteredpassword)   #for debugging
    #print(logindaten)                                                   #for debugging
    #print(usernamesinalist)                                             #for debugging


    for x in usernamesinalist:
        #print ("---",x,"---")                                           #for debugging
        if registration_enteredusername != x:
            uit = False
            pass
        if registration_enteredusername == x:
            uit = True
            break
    #print(uit)                                                          #for debugging
    if uit is False:
            logindaten[registration_enteredusername] = registration_enteredpassword
            registrationlabel.config(text="Sie sind registriert :)")
            registrationlabel.place(x=135, y=15)
    elif uit is True:
            registrationlabel.config(text = "Bitte benutzen sie ein anderen username!")
            registrationlabel.place(x=60, y=15)


def registrationWindow():
    global registrationlabel

    registrationWindow = tk.Toplevel(root)
    registrationWindow.geometry('410x210')
    registrationWindow.title('Registration')

    registrationlabel = tk.Label(registrationWindow, text="Registration")
    registrationlabel.place(x=175, y=15)

    global registration_usernameentry
    registration_usernameentry = tk.Entry(registrationWindow, fg="grey", borderwidth=0.5)
    registration_usernameentry.place(x=120, y=55)
    registration_usernameentry.insert(0, "username")
    registration_usernameentry.bind("<FocusIn>", registration_clearusernameentry)

    global registration_passwordentry
    registration_passwordentry = tk.Entry(registrationWindow, fg="grey", borderwidth=0.5)
    registration_passwordentry.place(x=120, y=85)
    registration_passwordentry.insert(0, "password")
    registration_passwordentry.bind("<FocusIn>", registration_clearpasswordentry)

    registration_btn = tk.Button(registrationWindow, borderwidth=0.5, text="Registrieren", command=newaccount)
    registration_btn.place(x=160, y=125)

    zurück_btn = tk.Button(registrationWindow, borderwidth=0.5, text="Zurück", command=registrationWindow.destroy)
    zurück_btn.place(x=175 , y=165)

def passwortcheck():
    global enteredusername
    global enteredpassword
    global setusername
    global setpassword
    global errolabel
    tuit = None

    enteredusername = usernameentry.get()
    enteredpassword = passwordentry.get()

    usernames = logindaten.keys()
    usernamesinalist = list(usernames)

    for y in usernamesinalist:
        if enteredusername != y:
            tuit = False
            pass
        if enteredusername == y:
            tuit = True
            i = y
            break

    if tuit is True:
        if enteredusername == i:
            password = logindaten.get(y)
            if enteredpassword == password:
                try:
                    errolabel.place_forget()
                except:
                    pass
                loginlabel.config(text="Sie sind eingeloggt")
                loginlabel.place(x=135, y=15)
                subwindow = tk.Toplevel(root)
                subwindow.geometry('410x210')
                nextwindow = tk.Label(subwindow, text="blub blub blub")
                nextwindow.pack()
            else:
                errolabel = tk.Label(root, text="username oder password falsch / Nicht dem System bekannt")
                errolabel.place(x=5, y=15)
    elif tuit is False:
        errolabel = tk.Label(root, text="username oder password falsch / Nicht dem System bekannt")
        errolabel.place(x=5, y=15)

def clearusernameentry(event):
    enteredusernameNORM = usernameentry.get()

    if enteredusernameNORM == "username":
        usernameentry.delete(0,"end")
    usernameentry.config(fg='black')


def clearpasswordentry(event):
    enteredpasswordNORM = passwordentry.get()

    if enteredpasswordNORM == "password":
        passwordentry.delete(0,"end")
    passwordentry.config(fg='black')



#------------------------------_GUI begins_------------------------------#
root = tk.Tk()
root.geometry('410x210')
root.title('Login')

loginlabel = tk.Label(root, text="Login")
loginlabel.place(x=175, y=15)

usernameentry = tk.Entry(root, fg="grey", borderwidth=0.5)
usernameentry.place(x=120, y=55)
usernameentry.insert(0, "username")
usernameentry.bind("<FocusIn>", clearusernameentry)


passwordentry = tk.Entry(root, fg="grey", borderwidth=0.5)
passwordentry.place(x=120, y=85)
passwordentry.insert(0, "password")
passwordentry.bind("<FocusIn>", clearpasswordentry)


btn1 = tk.Button(root, borderwidth=0.5, text="Login", command=passwortcheck)
btn1.place(x=180, y=125)

btn2 = tk.Button(root, borderwidth=0.5, text="Registrieren", command=registrationWindow)
btn2.place(x=160, y=165)

tk.mainloop()
