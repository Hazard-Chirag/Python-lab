import re

def isphone(num):
    pattern="^\+91[0-9]{10}$"
    if re.match(pattern,num):
        print("The phone number is ",num)

def isGmail(str):
    pattern="[0-9A-za-z._]+@gmail.com$"
    if re.match(pattern,str):
        print("The gmail is ",str)

with open("C:\coding\Python lab\sample.txt","r+") as file:
    rd=file.read()
    for str in rd.split("\n"):
        for word in str.split(","):
            isphone(word)
            isGmail(word)