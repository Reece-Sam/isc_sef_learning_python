# age = int(input("Enter your age: "))

# if age >= 100:
#     print("You are too old to sign")
# elif age >= 18:
#     print("Sign up successful!")
# elif age < 0:
#     print("You havent been born yet")
# else: 
#     print("Must be 18 and above") 


# response = input("Would you like food? (Y/N): ")

# if response == "Y":
#     print("Have some food!")
# else:
#     print("Ain't giving you shit!")


# name = input("Enter your name: ")

# if name == "":
#     print("you did not type in ur name beef!")
# else:
#     print(f"Hello {name}")

# for_sale = False

# if for_sale:
#     print("This item is for sale")
# else:
#     print("this item not for sale")


# online = True

# if online:
#     print("I am online")
# else:
#     print("Bro! im offline")


# #Exercise: Python calculator
# Operator = input("Enter operator:+,-,*,/ : ")
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# if Operator == "+": 
#     result = num1 + num2
#     print(round(result, 2))

# elif Operator == "-": 
#     result = num1 - num2
#     print(round(result, 2))

# elif Operator == "*": 
#     result = num1 * num2
#     print(round(result, 2))

# elif Operator == "/": 
#     result = num1 / num2
#     print(round(result, 2))

# else:
#     print(f"{Operator} is unknown")




#Python weight converter 

# weight = float(input("Enter your weight: "))
# unit = input("Kilograms or Pounds? (K or L): ")

# if unit == "K":
#     weight = weight * 2.205
#     unit == "Lbs."
#     print(f"Your weight is: {round(weight, 1)} {unit}")

# elif unit == "L":    
#     weight = weight / 2.205
#     unit = "kgs."
#     print(f"Your weight is: {round(weight, 1)} {unit}")

# else: 
#     print(f"{unit} was not valid")



#Exercise : Temperature convertor program
unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 2)
    print(f"The temp in Fahrenheit is: {temp}^F")

elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 2)
    print(f"The temp in Celsius is: {temp}^C")

else:
    print(f"{unit} is an invalid unit of measurement")

