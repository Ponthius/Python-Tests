""""marks = input("Enter your marks: ")
marks = int(marks)

try:
    if marks >= 90:
        print("Grade A")
    elif marks >= 80:
        print("Grade B")
    elif marks >= 70:
        print("Grade C")
    elif marks >= 50:
        print("Grade D")
    elif marks <= 40:
        print("Grade F")
    else:
        print("Invalid marks")
except ValueError:
    print("Please enter marks that are numbers eg 87")"""
    
    
"""num1 = int(input("Enter number: "))
operator = input("Choose an operator: + - / * ")
num2 = int(input("Enter number: "))

if operator == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operator == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operator == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operator == "/":
    if num2 == 0:
        print("Division by 0 is not possible")
    else:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
else:
    print("Invalid number")"""
    
    
"""temp = 30
raining = False
if temp > 28 and not raining:
    print("it's a good day")
else:
    print("It's not a good day")"""

"""name = "Poel"
ROLE = "member"
access = "Full Access" if ROLE == "admin" else "Limited Access"
print(access)"""

"""name = input("Enter your full name: ")
#result = len(name)
#result = name.find(" ")
#result = name.rfind("P")
result = name.isalpha()
print(result)"""


username = input("Enter username: ")
print(f"Valid Username" if len(username) <= 12 and not username.find(" ") == -1 and not username.isalpha() else "Welcome {username}")