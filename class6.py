def box(a, b=3):
    return a + b

sum = box(2)
print(sum)

def func(a,b):
    a+b

c = func(2,3)

print(c)

# string methods

name = "pakistan"

print(type(name))

print(name.capitalize())
print(name.count('a'))
print(name)
new_str = "my name is sami. my nationality is pakistani."

print(new_str.count('my'))
print(len(new_str))
print(new_str.find('my'))
print(new_str.index('my'))
print(new_str.replace("pakistani","american").upper())

# list methods
# append
# reverse
# sort
# insert
# remove
# pop
# extend

my_list = ["aneeq", "sami", "sohaib", "ayesha"," hifza" ]

# append:
my_list.append('Ameen Alam')
print(my_list)

# insert:
my_list.insert(1,'sir zia')
print(my_list)

# reverse:
my_list.reverse()
print(my_list)

# pop
print(my_list)
print(my_list.pop(2))

print(my_list)


# remove:
my_list.remove('sohaib')
print(my_list)


# sort:
my_list.sort(reverse=True)
print(my_list)



# extend:
new_faculty = ['Abdullah','Ghous']
print("old list", my_list)
my_list.extend(new_faculty)

print("updated list", my_list)


# Dictionary:

my_dict = {

       "name" : "john",
        "age" : 25,
        "city" : "karachi"

}

# dictionary methods

# get()
# keys()
# values()
# item()
# update()
# clear()
# pop()

# keys:
print(my_dict.keys())



# values:
print(my_dict.values())



# items:
print(my_dict.items())


# get:
print(my_dict.get("name"))


# update:
new_dict = {"city" : "Islamabad"}
new_dict2={"country":"pakistan"}
my_dict.update(new_dict)
my_dict.update(new_dict2)
print(my_dict)


# pop:
print(my_dict.pop('city'))
print(my_dict)


# clear:

my_dict.clear()
print(my_dict)