# Day 2: 30 Days of python programming
First_name = "Ghazali"
Last_name = "Muhammad"
Full_name = First_name + " " + Last_name
Country = "Nigeria"
City = "Gusau"
Age = 26
Year = 2026
is_married = False
is_true = True
is_light_on = True
Personal_info = {
    'name': 'Ghazali Muhammad',
    'age': 26,
    'is_learning': True
}


print("First Name:", First_name)
print("Last Name:", Last_name) 
print("Full Name:", Full_name)
print("Country:", Country)
print("City:", City)
print("Age:", Age)
print("Year:", Year)
print("Is Married:", is_married)
print("Is True:", is_true)
print("Is Light On:", is_light_on)
print("Personal Info:", Personal_info)

len(First_name)
len(Last_name)


print(type(First_name))
print(type(Last_name))
print(type(Full_name))
print(type(Country))
print(type(City))
print(type(Age))
print(type(Year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(Personal_info))

num_one = 5
num_two = 4
total = sum([num_one, num_two])
print(total)
diff = num_one - num_two
print(diff)
product = num_one * num_two
print(product)
division = num_one / num_two
print(division)
remainder = num_one % num_two
print(remainder)
floor_division = num_one // num_two
print(floor_division)
exp = num_one ** num_two
print(exp)


print("total:", total)
print("diff:", diff)
print("product:", product)
print("division:", division)
print("remainder:", remainder)
print("floor_division:", floor_division)
print("exponential:", exp)


import math
radius = int(input("Enter the radius of a circle: "))
area_of_circle = math.pi * (radius ** 2)
print(f"the circumference of the circle is: , {area_of_circle}")
circum_of_of_circle = 2 * math.pi * radius
print(f"the circumference of the circle is: , {circum_of_of_circle}")
Firstname = input("what is your first name? ")
print(Firstname)
Lastname = input("what is your last name? ")
print(Lastname)
Fullname = Firstname + " " + Lastname
print(Fullname)
Country = input("what country do you live in? ")
print(Country)
Age = input("what is your age? ")
print(Age) 

help(dir)

#Casting


# float to int
num_int = int(3.14)
print(num_int)

# int to float
num_float = float(5)
print(num_float)

# int to string
num_str = str(10)
print(num_str) 

#string to list
print(list("firstname"))