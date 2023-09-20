print("Enter the three test's marks")
test1=float(input())
test2=float(input())
test3=float(input())
if(test1<test2 and test1<test3):
    avg=(test2+test3)/2
elif(test2<test1 and test2<test3):
    avg=(test1+test3)/2
else:
    avg=(test1+test2)/2
print("Average of best of two tests is: "+str(avg))