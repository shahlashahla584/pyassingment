# range function/method

numbers = [1,2,3,4,5,6,7,8,9]
x = range(1,10)
# starting point
# condition
# increment
print(numbers)
print(list(x))

# aam zindagi
num: int = 2
print("2*1=",num*1)
print("2*2=",num*2)
print("2*3=",num*3)
print("2*4=",num*4)
print("2*5=",num*5)
print("2*6=",num*6)
print("2*7=",num*7)
print("2*8=",num*8)
print("2*9=",num*9)
print("2*10=",num*10)

# mintos zindagi
for num in range(1,11): # 1,2,3,4,......10
    print("2 x",num ,"=", 2 * num)


#f string ka use

for num in range (1,11):
    print(f" 2 x {num} = {2 * num}")


# loops
# two types of loop
# for loop
# while loop

num = 1
num = num + 1
print("num first time", num)
num = num + 1
print("num second time",num)
print(num < 10)
while num < 10:
     print("number before increment", num)
     num = num + 1
     print("number after increment", num)



password:str="python123"
user_input:str=""

print("user-input != password is", user_input!=password)
while user_input != password:
    print("incorrrect password!")   #user input wo baraber na ho password ka
    user_input = input("Type your answer plz!")



# for loop mein five ka table

for i  in range (1,11):
        print(f"5*{i} = {5*i}")




# string
# integar
# booean
# list
# tupple 

numbers = [1,2,3,4,5]
#           0   ,   1   ,   2    ,    3      
names1 = ["ALI", "Bilal","Hamza" ," okasha"]  # list mutable
#            0   ,   1   ,    2   ,     3
names2 = ("Ali" , "Bilal" , "Hamza", "Okasha") # tupple immutable

name: str = "Ali"
name = "Bilal"
   


# list
print ("names1 before over write" , names1)
#     Bilal  =   "Abdullah"     list ki values ko overwrite karsakte h
names1[1] = "Abdullah"
print("names1 after over write", names1)


# tuple
print("names1 before over write", names2)
#     Bilal   =  "Abdullah"    tuple ki values ko overwrite nhi karsakte error ayega
names2[1]  = "Abdullah"
print("names1 after over write", names2)


print("list first name is", names1[0])
print("tuple first name is", names2[0])




















 