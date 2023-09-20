import re
def isphonenum(str):
    pattern="(([0-9]){3}\-([0-9]){3}\-([0-9]){4})"
    result=re.match(pattern,str)
    if result:
        print("Success")
    else:
        print("Fail")

def normalphone(str):
    count=0
    for letter in str:
        if letter.isdigit():
            count+=1
    if(str[3]=='-' and str[7]=='-' and count==10):
        print("IT is suces")
    else:
        print("faile")

phone=input("Enter a phone number\n")
isphonenum(phone)
pone=input()
normalphone(pone)