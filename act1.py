def register():
    print("-----------REGISTRATION-------------")
    username = input("Enter Username: ")
    password = input("Enter Password: ")


    lis = [i.strip("\n") for i in open("username.txt")]
    
    if username in lis:
        print("User already exist")

    else:
        file = open("username.txt", "a")
        file.write(username+"\n")
        file.close()

        file2 = open("password.txt", "a")
        file2.write(password+"\n")
        file2.close()

        print("Registration Success")

    # for i in open("sample.txt"):
    #     i = "".join(i.split("\n"))
    #     if len(i) >= 14:
    #         data = i[10:]
    #         if data == username:
    #             print("User already exist, TRY AGAIN")
    #         else:
    #             file = open("sample.txt", "a")
    #             file.write("USER\n")
    #             print(username, file=username)
    #             print(password, file=password)
    #             file.close()
    #             print("Registration Success")
    #             break
            # if new[10:]:
            #     print(data)
            # else:
            #     ...
    
    # if username == data:
    #     print("User already exist, TRY AGAIN")
    # else:
    #     file = open("sample.txt", "a")
    #     file.write("username: " + username)
    #     file.write("\npassword: " + password + "\n" + "\n")
    #     file.close()
    #     print("Registration Success")
    
def login():
    print("-----------LOGIN-------------")
    uname = input("Enter username: ")
    pword = input("Enter password: ")

    usee = [i.strip() for i in open("username.txt")]
    passw = [i.strip() for i in open("password.txt")]
    
    if uname in usee:
        index = usee.index(uname)
        if index < len(passw) and passw[index] == pword:
            print("Login successful")
        else:
            print("Invalid username or password")
    else:
        print("Invalid username or password")


def update():
    print("-----------CHANGE PASSWORD-------------")
    uname = input("Enter current username: ")
    pword = input("Enter current password: ")
    new_pword = input("Enter new password: ")

    usee = [i.strip() for i in open("username.txt")]
    passw = [i.strip() for i in open("password.txt")]
    
    if uname in usee:
        index = usee.index(uname)
        if index < len(passw) and passw[index] == pword:
            passw[index] = new_pword
            
            with open("password.txt", "w") as f:
                for password in passw:
                    f.write(password + "\n")
            
            print("Password updated successfully.")
        else:
            print("Invalid username or password.")
    else:
        print("Invalid username or password.")


while True:
    print("(1) REGISTER\n(2) LOGIN\n(3) CHANGE PASSWORD")
    inp = input("COMMAND: ")
    print("(1) REGISTERN\n(2) LOGIN")
    if inp == "1":
        register()
    elif inp == "2":
        login()
    elif inp == "3":
        update()
        # resu = open("sample.txt").readlines(1)
        # result = "".join(resu)
        # print(result[10:])