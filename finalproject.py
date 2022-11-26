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
    user = input_new_user.get()
    passw = input_new_pasw.get()

    with open("info.json") as f:
        users_dct = json.load(f)
    if user in users_dct:
        output_sub.configure(text="username already exist !", fg="purple")
    elif len(passw) < 5 or passw.isalpha():
        output_sub.configure(text="please check your password", fg="purple")
    else:
        users_dct[user] = passw
        with open("info.json", "w") as f:
            json.dump(users_dct, f)
        output_sub.configure(text="submit done", fg="blue")


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
    if not islogin:
        output_logout.configure(text="you are already logged out", fg="purple")
    else:
        confirm = input("Are you sure you want to delete your account? YES OR NO")
        if confirm == "YES":
            islogin = False
            output_logout.configure(text="logged out successfully", fg="green")
        else:
            output_logout.configure(text="logout canceled", fg="purple")


def delete():
    global islogin

    if not (islogin):
        output_Dlt.configure(text="login first inorder to delete your account", fg="purple")
    else:
        with open("info.json") as f:
            users_dct = json.load(f)
        confirm = input("Are you sure you want to delete your account? yes/no")
        if confirm == "yes":
            users_dct.pop(islogin)
            with open("info.json", "w") as f:
                json.dump(users_dct, f)
            output_Dlt.configure(text="your account is deleted", fg="blue")
        else:
            output_Dlt.configure(text="delete was canceled", fg="purple")


def userslist():
    global islogin
    if islogin != "admin":
        output_userslist.configure(text="you are not allowed to this section", fg="purple")
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
lbl_login = tkinter.Label(win, text="Login")
lbl_login.pack()

lbl_user = tkinter.Label(win, text="UseName:")
lbl_user.pack()

in_user = tkinter.Entry(win, width=20)
in_user.pack()

lbl_pasw = tkinter.Label(win, text="Password:")
lbl_pasw.pack()
in_pasw = tkinter.Entry(win, width=20)
in_pasw.pack()

output = tkinter.Label(win, text="")
output.pack()

tkinter.Button(win, text="Login", command=login).pack(pady=10)

##################submit is here#################
lbl_submit = tkinter.Label(win, text="Submit")
lbl_submit.pack()

lbl_new_user = tkinter.Label(win, text="new UserName:")
lbl_new_user.pack()
input_new_user = tkinter.Entry(win, width=20)
input_new_user.pack()

lbl_new_pasw = tkinter.Label(win, text="New Password:")
lbl_new_pasw.pack()
input_new_pasw = tkinter.Entry(win, width=20)
input_new_pasw.pack()

output_sub = tkinter.Label(win, text="")
output_sub.pack()

tkinter.Button(win, text="Submit", command=submit).pack()

################login count is here###################
output_count = tkinter.Label(win, text="")
output_count.pack()

tkinter.Button(win, text="loginCount", command=showlogincount).pack()

########logout is here######## 

output_logout = tkinter.Label(win, text="")
output_logout.pack()

tkinter.Button(win, text="Logout", command=logout).pack()

##########delete is here#########
output_Dlt = tkinter.Label(win, text="")
output_Dlt.pack()

tkinter.Button(win, text="Delete", command=delete).pack()

###########userslist is here###############

output_userslist = tkinter.Label(win, text="")
output_userslist.pack()

tkinter.Button(win, text="UsersList", command=userslist).pack()

lst_box = tkinter.Listbox(win, height=20)
lst_box.pack()

win.mainloop()


























