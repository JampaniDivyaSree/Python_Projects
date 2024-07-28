import time

#set a password
password=98765
print("original password:",password)
n=True
while n:
    for i in range(5):

        #ask user to enter password
        user=int(input("enter password:"))
        if user==password:
            print("successful login")
            n=False
            break
        else:
            print("incorrect password")
    if n:    
        print("try after 30 seconds")
        print("-----------------------------")
        time.sleep(30)
        time.sleep(30)