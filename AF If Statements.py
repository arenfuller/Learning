#simple if statement
secret = "letmein"
username=input("enter username:")
password=input("enter password:")

if password == secret:
    print("Access Granted")
else:
    print("Access Denied")
