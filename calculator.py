class Calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    
    def calculate(self):
        if op=="/":
            print("divide of two number is =",self.num1/self.num2)
        elif op == "*":
            print("multiply of two number is =",self.num1*self.num2)
        elif op == "+":
            print("sum of two number is =",self.num1+self.num2)
        elif op == "-":
            print("subtract of two number is =",self.num1-self.num2)
        else:
            print("enter a valid operation")

print('''Welcome to Calculator 
    / for divide 
    * for multiplication
    + for addition
    - for subtraction''')
num1 = int(input("enter a first number -->>"))
num2 = int(input("enter a second number -->>"))
op = input("enter a operator  -->>")
num = Calculator(num1,num2)
num.calculate()


        