# 1. string
# 2. integer
# 3. boolean
# 4. list
# 5. tuple
# 6. dictionary

students = ["Ali", "Abdullah" , "Amir"]
student = ["Name" ,"01" , "Age" , 20, "class" ,"sunday 7-10"]
student = {
        "Name" : "Ali",
        "Age" : 20,
        "Class" : "sunday 7_10",
}

print("before",student)
student["Rollno"] = 9897

print("After",student)


def charger():
        print("charge mobile")

charger()



def ramo_kaka():
        print("hi")

        return "biryani bangayi"

plate = ramo_kaka()
print(plate)



a = 1
b = 4


# static function

def add():
        return a + b
sum = add()
print(sum)

# Dynamic function 
    
    # parameter

def greet(name, age, RollNo):
        print("Assalam o Alikum sir",name,"your age is", age,"roll no",RollNo,)

    # arument
greet("bilal", 20, 1234)


# version 1 static functions
num1:int = 10
num2:int = 10
def addition():
        print(num1 + num2)

addition()


 # version 2 dynamic functions
  # parameters

def addition(num1:int, num2: int):
        print(num1+num2)
               #arguments
addition(10,10)


# version 2 dynamic functions with return  

def additon(num1: int, num2: int):
        return num1 + num2

#print(addition(10,10))
# result = 20

result = addition(10,10)
print(result)
# final_result = 20 + 20
final_result = result  # / 20
print(final_result)


      
# Make a calculator using python 

def calculator (num1,num2,operation):
        if operation == "addition":
                return num1+num2
        elif operation == "subtraction":
                return num1-num2
        elif operation == "multiplication":
                return  num1*num2
        elif operation == "division":
                if num2 == 0:
                   return 'Division by zero is not allowed'
                return num1/num2
        else: 
                return"Invalid operation"
        
# main program

def main():
    print("welcome to my python calculator")
    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))
    print("Choose the operation to perform : Addition, Subtraction, Multiplication, Division")
    operation = input("Enter operation: ").strip().lower()
    result = calculator(num1, num2, operation)
    print(f"The result of  given numbers {operation} is: {result}")
    
main()






