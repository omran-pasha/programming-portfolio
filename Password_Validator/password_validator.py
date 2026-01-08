def validatepassword(passw):
    lowercount=0
    uppercount=0
    digitcount=0
    for char in passw:
        if char.islower():
            lowercount+=1
        elif char.isupper():
            uppercount+=1
        elif char.isdigit():
            digitcount+=1
        else:
            return False
    if lowercount<2 :
        return False,"The password is not valid,not enough lowercase characters"
    elif uppercount<2:
        return False,"The password is not valid,not enough uppercase characters"
    elif digitcount<3:
        return False,"The password is invalid,not enough digits"
    else:
        return True,"The password is valid"
while True:
    print("welcome to the password verifier: \nThis validator works on the following conditions: \n1.)There must be 2 lowercase characters \n2.)There must be 2 uppercase characters\n3.)There must be 3 digits")
    password=input("Enter the password :")
    valid,message=validatepassword(password)
    print(message)
    if valid:break
