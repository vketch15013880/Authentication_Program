##Password Validation Program



def mainMenu():
    logins={}

    username= input("Create a username:")
    password=input("Create a password:")

    logins[username] = password    
    for login in logins:
        print (logins)

def main():
    mainMenu()
    
    
if __name__ == "__main__":
    main()
