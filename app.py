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

"""
print(10**3)
x = 10
x = x + 3
x += 3
x = (10 + 3) * 2**2
print(x)
exponentiation 2**3
multiplication or division
addition or subtraction

x = (2 + 3) * 10 - 3
print(x)
"""

"""
import math

print(math.ceil(2.9))
print(math.floor(2.9))
print(math.cbrt(2))

x = 2.9
print(round(x))
print(abs(-2.9))
"""

# ------------------------ If Statement ------------------------ #

"""
if it`s hot
    It`s a hot day
    Drink plenty of water
otherwise if it`s cold
    It`s a cold day
    Wear warm clothes
otherwise
    It`s a lovely day        


is_hot = False
is_cold = False
if is_hot:
    print("It`s a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It`s a cold day")
    print("Wear warm clothes")
else:
    print("It`s a lovely day")
print("Enjoy your day")

price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment= 0.2 * price
print(f"Down payment: ${down_payment}")
"""
