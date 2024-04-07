class student:
    def __init__(self,name):
        self.name = name
        self.marks = []
    def enter_marks(self):
            for i in range(3):
                n = int(input("Enter the marks: %s in subject:  %d"%(self.name,i+1)))
                self.marks.append(n)
    def display(self):
        print(self.name,'got',self.marks)

p1 = student('Sourasish',)
p1.enter_marks()
p2 = student('rakesh')
p2.enter_marks()
p3 = student('tamal')
p3.enter_marks()
