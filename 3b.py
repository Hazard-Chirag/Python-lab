def similarity(str1,str2):
    k=0
    i=min(len(str1),len(str2))
    for j in range(0,i):
        if(str1[j]==str2[j]):
            k+=1
    return k

str1=input("Enter first string")
str2=input("Enter second string")
count=similarity(str1,str2)
print("The number of letters matched in two strings is:",count)
print("The similarity percentage is: ",(count/max(len(str1),len(str2))*100))