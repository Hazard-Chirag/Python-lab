class Employee:
    def __init__(self,ename,esal,edept):
        self.name=ename
        self.sal=esal
        self.dept=edept
    
    def updatesal(self,sal,dept):
        if(dept==self.dept):
            self.sal=sal
    

Emp=[]
n=int(input("Enter the number of employees"))
for i in range(n):
    name=input("Enter name")
    dept=input("Enter dept")
    sal=int(input("Enter salary"))
    emp1=Employee(name,sal,dept)
    Emp.append(emp1)
for i in range(n):
    print(Emp[i].name,"",Emp[i].sal)
