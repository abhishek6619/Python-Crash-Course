# ------------------------ Varibale ------------------------ #

# price = 10
# rating = 4.4
# name = "Abhishek"
# is_published = True
# print(price)

# Ques: We check in a patient named John Smith. He's 20 years old and is a new patient

# full_name = "John Smith"
# age = 20
# is_new_Patient = True

# ------------------------ Receiving Input ------------------------ #

# name = input("What is yout name? ")
# print("Hi " + name)

# Ques: Ask two questions: person's name and favourite color. Then, print a message like "Mosh like blue"

# name = input("What is yout name? ")
# favourite_color = input("What is yout favourite color? ")
# print(name + " likes " + favourite_color)

# ------------------------ Type Conversion ------------------------ #

# birth_year = input("Birth year: ")
# print(type(birth_year))
# age = 2025 - int(birth_year)
# print(type(age))
# print(age)

# Ques: Ask a user their weight (in pounds), convert it to kilograms and print on the terminal

# weight_lbs = float(input("Weight (lbs): "))
# weight_kg = weight_lbs * 0.45
# print(weight_kg)

# ------------------------ String ------------------------ #

# course = '''
# Hi John

# Here is our first email to you

# Thank you
# The Support team
# '''
# course = "Python for Beginners"
# another = course[:]

# print(course[:])
# print(another)

# ------- Formatted String ------- #

# first = "John"
# last = "Smith"
# # John [Smith] is  a coder
# message = first + " [" + last + "] is a coder"
# msg = f"{first} [{last}] is a coder"
# print(msg)
# print(message)

# ------- String Methods ------- #

# course = "Python for Beginners"
# print(len(course))
# print(course.upper())
# print(course.lower())
# print(course.find("Beginners"))
# print(course.replace("Beginners", "Absolute Beginners"))
# print(course.replace("P", "J"))
# print("python" in course)

# ------------------------ Arithmetic Operations ------------------------ #

# print(10**3)
# x = 10
# x = x + 3
# x += 3
# x = (10 + 3) * 2**2
# print(x)
# exponentiation 2**3
# multiplication or division
# addition or subtraction
# x = (2 + 3) * 10 - 3
# print(x)

# import math
# print(math.ceil(2.9))
# print(math.floor(2.9))
# print(math.cbrt(2))

# x = 2.9
# print(round(x))
# print(abs(-2.9))

# ------------------------ conditionals Statement ------------------------ #

# if it`s hot
#     It`s a hot day
#     Drink plenty of water
# otherwise if it`s cold
#     It`s a cold day
#     Wear warm clothes
# otherwise
# It`s a lovely day

# is_hot = False
# is_cold = False
# if is_hot:
#     print("It`s a hot day")
#     print("Drink plenty of water")
# elif is_cold:
#     print("It`s a cold day")
#     print("Wear warm clothes")
# else:
#     print("It`s a lovely day")
# print("Enjoy your day")

# price = 1000000
# has_good_credit = True

# if has_good_credit:
#     down_payment = 0.1 * price
# else:
#     down_payment = 0.2 * price
# print(f"Down payment: ${down_payment}")

# # ------- Logical operators ------- #

# has_high_income = True
# has_good_credit = True


# if has_high_income or has_good_credit:
#     print("Eligible for loan")
# has_good_credit = True
# has_criminal_record = False

# if has_good_credit and not has_criminal_record:
#     print("Eligible for loan")

# temperature = 35

# if temperature > 30:
#     print("It`s a hot day")
# else:
#     print("It`s not a hot day")

# # ------- Comparison operators ------- #

# name = "Abhishek Kumar Singh"
# if len(name) < 3:
#     print("Name must be at least 3 characters")
# elif len(name) > 50:
#     print("Name can be a maximum of 50 characters")
# else:
#     print("Name looks good!")

# weight = int(input("Weight: "))
# unit = input("(L)bs or (K)g: ")
# if unit.upper() == "L":
#     converted = weight * 0.45
#     print(f"You are {converted} kilos")
# else:
#     converted = weight / 0.45
#     print(f"You are {converted} pounds")

# ------------------------ Looping Statement ------------------------ #

# i = 1
# while i <= 5:
#     print("* " * i)
#     i = i + 1
# print("Done")

# Number Guessing

# secret_number = 9
# guess_count = 0
# guess_limi = 3
# while guess_count < guess_limi:
#     guess = int(input("Guess: "))
#     guess_count += 1
#     if guess == secret_number:
#         print("You won!")
#         break
# else:
#     print("Soory, you failed!")

# Building Car game

# command = ""
# started = False
# while command.lower() != "quit":
#     command = input("> ")
#     if command == "start":
#         if started:
#             print("Car is already started...")
#         else:
#             started = True
#             print("Car started...")
#     elif command == "stop":
#         if not started:
#             print("car is already stopped!")
#         else:
#             started = False
#             print("car stopped.")
#     elif command == "help":
#         print(
#             """
#             start - to start the car
#             stop - to stop the car
#             quit - to quit
#             """
#         )
#     elif command == "quit":
#         break

# print("Sorry, I don`t understand that!")

# ------- for loop ------- #

# for item in range(5, 10, 2):
#     print(item)

# prices = [10, 20, 30]

# total = 0
# for price in prices:
#     total += price
# print(f"Total: {total}")

# for x in "Python":
#     print(x)

# for x in ["a", "b", "c"]:
#     print(x)

# for x in range(0, 10, 2):
#     print(x)

# print(type(range(5)))
# print([1, 2, 3, 4, 5])

# names = ["John", "Mary"]
# for name in names:
#     if name.startswith("J"):
#         print("Found")
#         break
# else:
#     print("Not found")

# ------- while loop ------- #

# guess = 0
# answer = 5

# while answer != guess:
#     guess = int(input("Guess: "))
# else:
#     pass

# ------------------------ Function ------------------------ #


# def increment(number: int, by: int = 1) -> tuple:
#     return (number, number + by)


# print(increment(2, by=3))
# print(increment(2))

# ------- args ------- #


# def multiply(*list):
#     total = 1
#     for number in list:
#         total *= number
#     return total


# print(multiply(2, 3, 4, 5))


# def save_user(**user):
#     print(user["name"])


# save_user(id=1, name="admin")

# ------- Scope ------- #

# message = "a"


# def greet():
#     global message
#     message = "b"
#     # print(message)


# greet()
# print(message)

# ------- Debugging ------- #


# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total


# print("start")
# print(multiply(1, 2, 3))
# print("finish")


# Q: fizz_buzz Problem


def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "Fizz Buzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input


print(fizz_buzz(15))
print(fizz_buzz(3))
print(fizz_buzz(5))
