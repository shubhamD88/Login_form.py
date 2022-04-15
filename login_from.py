#login form
username = input("enter user name : ")
password = input("enter password : ")
print("singup done")

username2 = input("enter user name : ")
password2 = input("enter password : ")

if username == username2 and password == password2 :
    print("Log in done")
elif username == username2 and password != password2:
    print("check your password")
elif username!= username2 and password == password2:
    print("check your user name")
else:
    print("check your id and password  ")
