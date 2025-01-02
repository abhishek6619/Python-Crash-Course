# Introduction to Python

## Variables

We use variables to temporarily store data in computer’s memory.
```bash
price = 10
rating = 4.9
course_name = ‘Python for Beginners’
is_published = True
```
In the above example,<br>
• price is an integer (a whole number without a decimal point)<br>
• rating is a float (a number with a decimal point)<br>
• course_name is a string (a sequence of characters)<br>
• is_published is a boolean. Boolean values can be True or False.

## Comments

We use comments to add notes to our code. Good comments explain the hows and whys, not what the code does. That should be reflected in the code itself. Use comments to add reminders to yourself or other developers, or also explain your assumptions and the reasons you’ve written code in a certain way.
```bash
This is a comment and it won’t get executed.
Our comments can be multiple lines
```

### Receiving Input

We can receive input from the user by calling the input() function.

```bash
birth_year = int(input(‘Birth year: ‘))
```

The input() function always returns data as a string. So, we’re converting the result into an integer by calling the built-in int() function.

## Strings

We can define strings using single (‘ ‘) or double (“ “) quotes. <br>
To define a multi-line string, we surround our string with tripe quotes (“””).

We can get individual characters in a string using square brackets []

```bash
course = ‘Python for Beginners’
course[0] # returns the first character
course[1] # returns the second character
course[-1] # returns the first character from the end
course[-2] # returns the second character from the end
```

We can slice a string using a similar notation:<br>
```bash
course[1:5]
```

The above expression returns all the characters starting from the index position of 1 to 5 (but excluding 5). The result will be ytho.<br>
If we leave out the start index, 0 will be assumed.<br>
If we leave out the end index, the length of the string will be assumed.<br>

We can use formatted strings to dynamically insert values into our strings:

```bash
name = ‘Abhishek’
message = f’Hi, my name is {name}’
message.upper() # to convert to uppercase
message.lower() # to convert to lowercase
message.title() # to capitalize the first letter of every word
message.find(‘p’) # returns the index of the first occurrence of p
(or -1 if not found)
message.replace(‘p’, ‘q’)
```

To check if a string contains a character (or a sequence of characters), we use the in
operator:

```bash
contains = ‘Python’ in course
```

## Arithmetic Operations

```bash
+
-
*
/  # returns a float
// # returns an int
%  # returns the remainder of division
** # exponentiation - x ** y = x to the power of y
```

Augmented assignment operator:
```bash
x = x + 10
x += 10
```

### Operator precedence:
1. parenthesis
2. exponentiation
3. multiplication / division
4. addition / subtraction

## If Statements

```bash
if is_hot:
print(“hot day”)
elif is_cold:
print(“cold day”)
else:
print(“beautiful day”)
```
Logical operators:
```bash
if has_high_income and has_good_credit:
...
if has_high_income or has_good_credit:
...
is_day = True
is_night = not is_day
```

## Comparison operators
```bash
a > b
a >= b (greater than or equal to)
a < b
a <= b
a == b (equals)
a != b (not equals)
```