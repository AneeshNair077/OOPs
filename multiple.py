class Calculation1:
    def add(self,a,b):
        return a+b
class Calculation2:
    def subtraction(self,a,b):
        return a-b
class Calculation3:
    def multiplication(self,a,b):
        return a*b
class Calculator(Calculation1,Calculation2,Calculation3):
    def divide(self,a,b):
        return a/b
d=Calculator()
print(d.add(10,20))
print(d.multiplication(10,20))
print(d.subtraction(20,4))
print(d.divide(10,20))