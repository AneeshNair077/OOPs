class School:
    def open(self):
        print("School open")
class Class1(School):
    def started(self):
        print("Class started")
class Student(Class1):
    def present(self):
        print("Students presented")
d=Student()
d.open()
d.started()
d.present()