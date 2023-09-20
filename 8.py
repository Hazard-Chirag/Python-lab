class Palistr:
    def __init__(self):
        self.ispali=False
    
    def check(self,str):
        if(str==str[::-1]):
            self.ispali=True
        else:
            self.ispali=False
        return self.ispali
    
class PaliInt(Palistr):
    def __init__(self):
        self.ispali=False
    def check(self,num):
        temp=num
        rev=0
        while(num>0):
            rem=num%10
            rev=(rev*10)+rem
            num=num//10
        if rev==temp:
            self.ispali=True
        else:
            self.ispali=False
        return self.ispali

str=input("Enter the string")

stobj=Palistr()
if stobj.check(str):
    print("YEes")
else:
    print("No")

val=int(input("Enter a number"))

intobj=PaliInt()

if intobj.check(val):
    print("YES")
else:
    print("no")


