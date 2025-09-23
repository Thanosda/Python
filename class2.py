class calculator:
    def __init__(self):
        self.num1=0
        self.num2=0
    def add(self):
        print(self.num1+self.num2)
    def sub(self):      
         print(self.num1-self.num2)
    def mul(self):
         print(self.num1*self.num2) 
    def div(self):
         print(self.num1/self.num2) 
calc=calculator()
calc.num1=34443
calc.num2=2344
calc.add()
calc.sub()
calc.mul()
