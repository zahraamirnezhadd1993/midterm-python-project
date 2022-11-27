import json
import tkinter



islogin=False
def login():
    global islogin
    user = in_user.get()
    passw = in_pasw.get()

    if (islogin):
        output.configure(text="you are  loggedin now", fg="purple")
        return
    else:

        with open("info.json") as f:
            users_dct = json.load(f)
        if user in users_dct and users_dct[user] == passw:
            output.configure(text="welcome to your account", fg="blue")
            islogin = user
            logincount()
            
#### ba inke chand bar dastoro check kardam natonestam pak konam entry bad az vorord kar nemikone:(            
            in_user.delete(0,"end")
            in_pasw.delete(0,"end")
        else:
            output.configure(text="wrong username or password", fg="purple")



def logincount():
    global islogin
    with open("logincount.json") as f:
        logincount = json.load(f)
    if islogin in logincount:
        logincount[islogin] += 1
    else:
        logincount[islogin] = 1
    with open("logincount.json", "w") as f:
        json.dump(logincount, f)


def submit():
    user = in_user2.get()
    passw = in_pasw2.get()

    with open("info.json") as f:
        users_dct = json.load(f)
    if user in users_dct:
        submitx.configure(text="username already exist !", fg="purple")
    elif len(passw) < 5 or passw.isalpha():
        submitx.configure(text="please check your password", fg="purple")
    else:
        users_dct[user] = passw
        with open("info.json", "w") as f:
            json.dump(users_dct, f)
        submitx.configure(text="submit done", fg="blue")
        
#### kar nemikone dastore payiin :(
        in_user2.delete(0,"end")
        in_pasw2.delete(0,"end")


def showlogincount():
    global islogin

    if islogin != "admin":
        output_count.configure(text="you are not allowed to this section", fg="purple")
        return
    else:
        with open("logincount.json") as f:
            logincount = json.load(f)
        output_count.configure(text=logincount)


def logout():
    global islogin
    if(not(islogin)):
        logoutx.configure(text="now,you are  loggedout plz login", fg="purple")
    else:
        confirm = input("Are you sure  to delete your account? YES OR NO? __")
        if confirm == "YES":
            islogin = False
            logoutx.configure(text="logged out successfully", fg="green")
        else:
            logoutx.configure(text="logout is not done", fg="purple")


def delete():
    global islogin

    if (not(islogin)):
        deletex.configure(text="plz login first for deletng your account", fg="purple")
    else:
        with open("info.json") as f:
            users_dct = json.load(f)
        confirm = input("Are you sure to delete your account??? YES/NO? __")
        if( confirm == "YES"):
            users_dct.pop(islogin)
            with open("info.json", "w") as f:
                json.dump(users_dct, f)
            deletex.configure(text="it is done,you dont have any account here,anymore", fg="blue")
        else:
            deletex.configure(text="delete was canceled", fg="purple")


def userslist():
    global islogin
    if (islogin != "admin"):
        userslistx.configure(text="you can not access to this part,sry", fg="purple")
        return
    else:
        with open("info.json") as f:
            userslist = json.load(f)
        usr_lst = str(list(userslist.keys()))
        lst_box.insert("end", usr_lst)






win=tkinter.Tk()
win.title("win")
win.geometry("500x750")
win.resizable(False,False)


#############login is here######################
output = tkinter.Label(win, text="")
output.pack()

lbl_login = tkinter.Label(win, text="Login")
lbl_login.pack()

lbl_user = tkinter.Label(win, text="UserName:")
lbl_user.pack()

in_user = tkinter.Entry(win, width=20)
in_user.pack()

lbl_pasw = tkinter.Label(win, text="Password:")
lbl_pasw.pack()

in_pasw = tkinter.Entry(win, width=20)
in_pasw.pack()


login_btn=tkinter.Button(win, text="Login", command=login)
login_btn.pack()

##################submit is here#################

submitx= tkinter.Label(win, text="")
submitx.pack()

lbl_submit = tkinter.Label(win, text="Submit")
lbl_submit.pack()

lbl_user2 = tkinter.Label(win, text="new UserName:")
lbl_user2.pack()
in_user2 = tkinter.Entry(win, width=20)
in_user2.pack()

lbl_pasw2 = tkinter.Label(win, text="New Password:")
lbl_pasw2.pack()
in_pasw2= tkinter.Entry(win, width=20)
in_pasw2.pack()



submit_btn=tkinter.Button(win, text="Submit", command=submit)
submit_btn.pack()

################login count is here###################
output_count = tkinter.Label(win, text="")
output_count.pack()

count_btn=tkinter.Button(win, text="loginCount", command=showlogincount)
count_btn.pack()

########logout is here######## 

logoutx = tkinter.Label(win, text="")
logoutx.pack()

logout_btn=tkinter.Button(win, text="Logout", command=logout)
logout_btn.pack()

##########delete is here#########
deletex = tkinter.Label(win, text="")
deletex.pack()

delete_btn=tkinter.Button(win, text="Delete", command=delete)
delete_btn.pack()

###########userslist is here###############

userslistx= tkinter.Label(win, text=" ")
userslistx.pack()

userlist_btn=tkinter.Button(win, text="UsersList", command=userslist)
userlist_btn.pack()

lst_box = tkinter.Listbox(win, height=20)
lst_box.pack()

win.mainloop()


























