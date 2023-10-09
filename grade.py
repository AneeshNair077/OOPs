class Grade:

    def __init__(self,name,mark1,mark2,mark3):
        self.name=name
        self.m1=mark1
        self.m2=mark2
        self.m3=mark3
    def grading(self):
        avg=(self.m1+self.m2+self.m3)/3
        if(avg>90 and avg<=100):
            print("A grade")
        elif(avg<=90 and avg>80):
            print("B grade")
        elif (avg <= 80 and avg > 70):
            print("C grade")
        elif (avg <= 70 and avg > 60):
            print("D grade")
        elif (avg <= 60 and avg > 50 ):
            print("Pass")
        else:
            print("Fail")

name=input("Enter name of student: ")
mark1 = int(input("Enter marks in 1st subject: "))
mark2 = int(input("Enter marks in 2nd subject: "))
mark3 = int(input("Enter marks in 3rd subject: "))
g=Grade(name,mark1,mark2,mark3)
g.grading()




