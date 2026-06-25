password=input("Enter Password :")
length=len(password)
if length<6:
    print("weak password")
elif 6<=length <=10:
    print("medium password")
else:
    print("strong password")
print("-----------------------")
print("Code Excecuted Successfully..")
input("Please Click Enter to Exit")
