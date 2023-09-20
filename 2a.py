def fn(N):
    if(N==1):
        return 0
    elif(N==2):
        return 1
    else:
        return fn(N-1)+fn(N-2)

n=int(input("Enter a number greater than 0"))
if(n<0):
    print("Error")
else:
    print("The value after evaluation is ",fn(n))