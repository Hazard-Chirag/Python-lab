def Romantodec(str):
    dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    str=str[::-1]
    p=str[0]
    sum=dict[p]
    for i in str[1:]:
        if(dict[p]<=dict[i]):
            sum+=dict[i]
        else:
            sum-=dict[i]
            p=i
    return sum

str=input("Enter Roman number\n")
print(Romantodec(str))