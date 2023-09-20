def bin_to_dec(num):
    i=0
    sum=0
    while(num>0):
        rem=num%10
        sum=sum+rem*(2**i)
        i+=1
        num=num//10
    return sum

def oct_to_dec(num):
    i=0
    sum=0
    while(num>0):
        rem=num%10
        sum+=rem*(8**i)
        num=num//10
        i+=1
    return sum

def oct_to_hex(num):
    n=oct_to_dec(num)
    list=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    hex=""
    while(n>0):
        hex=list[n%16]+hex
        n=n//16
    return hex

num=int(input("Enter a binary Number"))
print("The decimal equivalent",bin_to_dec(num))
num=int(input("Enter a octal number"))
print("The hexadecimal equivalent is",oct_to_hex(num))