from abc import ABC
class Calculator(ABC):
    def add1(self):
        print('Addition')
class Calculator1(Calculator):
    def sub(self):
        print("Sub")
class Calculator2(Calculator):
    def multi(self):
        print("multi")
c=Calculator2()
c.add1()
c.multi()
d=Calculator1()
d.sub()
d.add1()