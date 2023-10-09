class Employee:
    def __init__(self,name,sal):
        self.ename=name
        self.esal=sal
    def salarycalc(self):
        if(self.esal<=500000 and self.esal>400000):
            bonus=0.2*self.esal
        elif(self.esal <= 400000 and self.esal > 300000):
            bonus = 0.1 * self.esal
        elif (self.esal <= 300000 and self.esal > 200000):
            bonus = 0.05 * self.esal
        else:
            bonus=0
        netsal=bonus+self.esal
        print("Net salary=",netsal)
name=input("Enter name of employee: ")
sal=int(input("Enter salary: "))
e=Employee(name,sal)
e.salarycalc()




