def InsertionSort(list):
    for i in range(len(list)):
        temp=list[i]
        j=i-1
        while(j>=0 and list[j]>temp):
            list[j+1]=list[j]
            j-=1
        list[j+1]=temp

def merge(Llist,Rlist):
    lindex,rindex=0,0
    NewList=[]
    while(lindex<len(Llist) and rindex<len(Rlist)):
        if(Llist[lindex]<Rlist[rindex]):
            NewList.append(Llist[lindex])
            lindex+=1
        else:
            NewList.append(Rlist[rindex])
            rindex+=1
    while(lindex<len(Llist)):
        NewList.append(Llist[lindex])
        lindex+=1
    while(len(Rlist)>rindex):
        NewList.append(Rlist[rindex])
        rindex+=1
    return NewList

def mergesort(list):
    if(len(list)<=1):
        return list
    mid=len(list)//2
    Llist=list[0:mid]
    Rlist=list[mid:]
    Llist=mergesort(Llist)
    Rlist=mergesort(Rlist)
    return merge(Llist,Rlist)
def main():
    n=int(input("Enter size of an array\n"))
    print("Enter elements of an array")
    List=[]
    for i in range(n):
        List.append(int(input()))
    print("Initial array:\n",List)
    print("Merge sorted array: \n",mergesort(List))
    n=int(input("Enter size of an array\n"))
    print("Enter elements of an array")
    for i in range(n):
        list.append(int(input()))
    print("Initial array:\n",list)
    InsertionSort(list)
    print("Insertion sorted array:\n",list)
main()
