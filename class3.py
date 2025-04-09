# if/else

if False:
    print("condition is true")
else:
    print("condition is false")


#comparision operators  True/False

num:int = 10
print(num < 10 )
# num > 0 = True
print(num > 0) # True
if num > 0:     
    print("number is positive")

else:
   print("number is negative")


num:int = 100
# True  and False
print(num > 0 and num < 100)
if num > 0 and num < 100:
    print("number is positive")
else: 
    print("nmber is negative")


name:str = "miss shahla" 
if name == "miss sana": 
   print("welcome miss sana")
else:
    ("Aap kon")
print("kaise hai ap")

#(snake case)
# time_of_day: str = "abc"

if "time_of_day" == "morning" :
    print("Good Morning")

elif "time_of_day" == "afternoon": 
    print("Good Afternoon")

elif "time_of_day" == "evening": 
    print("Good Evening")
else:
    print ("Good Night")
        




numbers = [1,2,3,4,5,6,7,8,9,10]
print("Aam zindagi")
print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])
print(numbers[4])

print("Mintos zindagi")
for num in numbers:
    print(num)

 
# string
# integar
# boolean
# list
name = "sir Ali"
#                        0     ,        1      ,     2
names: list[str] = ["sir Aneeq", "sir sohaib","sir sami"]
#                   0,1,2,3,4

print(names)
print(names[1])
print(numbers[4])
numbers[0] # -> 1
# if numbers[0] > 1:


print(range(5))
res = range(1,5)
# starting point
# condition 
# increment

print(numbers)
number2 = list(range(1,5))
print(number2)
print(list[range(1,5)])
numbers: list[int] = [1,2,3,4,5]


# for loop
# iterables
numbers: list[int] = [1,2,3,4,5] # iterable
print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])
print(numbers[4])

# for variable in iterablr:
num = numbers[0] 
num = numbers[1]
for n in numbers:
    print("n is",n)



numbers = [1,2,3,4,5,6,7,8,9,10]
print("Aam zindagi")
print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])
print(numbers[4])

print("Mintos zindagi")
for num in numbers:
    print(num)







