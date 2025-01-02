# ------------------------ Varibale ------------------------ #

"""
price = 10
rating = 4.4
name = "Abhishek"
is_published = True
print(price)
"""

# Ques: We check in a patient named John Smith. He's 20 years old and is a new patient
"""
full_name = "John Smith"
age = 20
is_new_Patient = True
"""

# ------------------------ Receiving Input ------------------------ #

"""
name = input("What is yout name? ")
print("Hi " + name)
"""

# Ques: Ask two questions: person's name and favourite color. Then, print a message like "Mosh like blue"
"""
name = input("What is yout name? ")
favourite_color = input("What is yout favourite color? ")
print(name + " likes " + favourite_color)
"""

# ------------------------ Type Conversion ------------------------ #

"""
birth_year = input("Birth year: ")
print(type(birth_year))
age = 2025 - int(birth_year)
print(type(age))
print(age)
"""

# Ques: Ask a user their weight (in pounds), convert it to kilograms and print on the terminal

"""
weight_lbs = float(input("Weight (lbs): "))
weight_kg = weight_lbs * 0.45
print(weight_kg)
"""

# ------------------------ String ------------------------ #

"""
# course = '''
# Hi John

# Here is our first email to you

# Thank you
# The Support team
# '''
course = "Python for Beginners"
another = course[:]

# print(course[:])
print(another)
"""

# ------- Formatted String ------- #

"""
first = "John"
last = "Smith"
# John [Smith] is  a coder
message = first + " [" + last + "] is a coder"
msg = f"{first} [{last}] is a coder"
print(msg)
print(message)
"""

# ------- String Methods ------- #

"""
course = "Python for Beginners"
print(len(course))
print(course.upper())
print(course.lower())
print(course.find("Beginners"))
print(course.replace("Beginners", "Absolute Beginners"))
print(course.replace("P", "J"))
print("python" in course)
"""

# ------------------------ Arithmetic Operations ------------------------ #

""""""
print(10**3)
x = 10
# x = x + 3
x += 3
print(x)
