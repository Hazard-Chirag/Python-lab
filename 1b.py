def palindrome(num):
    rev=0
    temp=num
    while(num>0):
        rem=num%10
        rev=(rev*10)+rem
        num=num//10
    if(rev==temp):
        return True
    else:
        return False

def occurence(num):
    list=[int(x) for x in str(num)]
    for x in set(list):
        print(str(x)+"has occured",list.count(x),"number of times")

num=int(input("Enter a number"))
if(palindrome(num)):
    print("It is palindrome")
else:
    print("Not a palindrome")
occurence(num)