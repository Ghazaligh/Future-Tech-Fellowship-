# 1. Empty dictionary called dog
dog = {}

# 2. Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Buddy'
dog['color'] = 'Brown'
dog['breed'] = 'german shepherd'
dog['legs'] = 4
dog['age'] = 3

print("Dog dictionary:", dog)

# 3. Create a student dictionary with required keys
student = {
    'first_name': 'Ghazali',
    'last_name': 'Bashar',
    'gender': 'Male',
    'age': 26,
    'marital_status': 'Single',
    'skills': ['Python', 'Data Analysis'],
    'country': 'Nigeria',
    'city': 'Gusau',
    'address': 'FCE, Gusau, Zamfara State'
}

print("\nStudent dictionary:", student)

# 4. Get the length of the student dictionary
print("\nLength of student dictionary:", len(student))

# 5. Get the value of skills and check data type
skills = student['skills']
print("\nSkills:", skills)
print("Data type of skills:", type(skills))


# 6. Modify the skills by adding one or two skills
student['skills'].append('SQL')
student['skills'].append('Machine Learning')

print("\nUpdated skills:", student['skills'])


# 7. Get dictionary keys as a list
keys_list = list(student.keys())
print("\nKeys:", keys_list)


# 8. Get dictionary values as a list
values_list = list(student.values())
print("\nValues:", values_list)


# 9. Change dictionary to list of tuples using items()
items_list = list(student.items())
print("\nDictionary as list of tuples:", items_list)


# 10. Delete one item from the dictionary
del student['address']
print("\nAfter deleting 'address':", student)


# 11. Delete the entire dictionary
del student

# Uncomment the next line to confirm deletion (will raise error)
# print(student)