# string method:
name = "pakistan"
# capatalize
# count
# index
# lenght
# find
# replace
print(name.capitalize())
name = "pakistan"

print(name.count('a'))
newName = 'my name is Aneeq and my nationality is pakistani'
print(newName.find("is"))


# Lenght:
newName = 'my   name is Aneeq and ny nationality is pakistan'
name_count = len(newName)  # snake_case
print(name_count)


# replace:
new_name:str = 'my name is Aneeq and my nationality is pakistan'
print(new_name.replace('pakistan','America'))

# list:
my_list = ['Ali','Abdullah', 'Amir']
# Append:
my_list.append('Asif')
print(my_list)

# insert:
my_list.insert(-1,"sabir")
print(my_list)
print(my_list[-1])

# reverse:
my_list.reverse()
print(my_list)

# pop:
my_list.pop()
my_list.pop(0)
print(my_list)

# extend:
my_list = ['Asif','Ali','Amir']
new_list = ['Ali','Aneeq','Abdullah']
my_list.extend(new_list)

my_list.remove('Ali')

# sort:
num_list = [5,2,9,1,7]
num_list.reverse()
print(f"reverse list {num_list}")
num_list.sort(reverse=True)
print(f"sort list {num_list}")

# try except
num: int = 10
num2: int = 0

user_input = input("Enter your number")
result = num / num2
print(result)


# try:
result = num / num2
print(result)

# except Exception as e:
# print(e)


# zero division error
# key error
# index error
# value error
# import error

list = ["ali","abdullah"]

try:
    result = list[3]
    print(result)
except IndexError:
    print("this is error with index")
except ZeroDivisionError:
    print("this is error for zero value")




