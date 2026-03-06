# name = input("Enter your name: ")

# while name == "":
#     print("You did not enter your name")
#     name = input("Enter your name: ")
# else:
#     print(f"Hello {name}")


# age = int(input("Enter your age: "))

# while age < 0:
#     print("Age can't be negative")
#     age = int(input("Enter your age: "))

# print(f"You are {age} years old")


#used the logical not
# food = input("Enter a food you like (q to quit): ")

# while not food == "q" :
#     print(f"You like {food}")
#     food = input("Enter another food you like(q to quit): ")

# print("bye")


#used the logical or
# num = int(input("Enter a # between 1 - 10: "))

# while num < 1 or num > 10:
#     print(f"{num} is not valid")
#     num = int(input("Enter a # between 1 - 10: "))

# print(f"Your number is {num}")




# ===Exercise===
#Python compound interest calculator 

principle = 0
rate = 0
time = 0 

# while principle <= 0: 
#     principle = int(input("Enter the principle amount: "))
#     if principle <= 0:
#         print("Principle cant be less than or equal to zero")

# while rate <= 0: 
#     rate = float(input("Enter the interest rate: "))
#     if rate <= 0:
#         print("Interest rate cant be less than or equal to zero")

# while time <= 0: 
#     time = int(input("Enter the time in years: "))
#     if principle <= 0:
#         print("Time cant be less than or equal to zero")

# #formular to calculate compound interest
# total = principle * pow((1 + rate / 100), time)

# print(f"Balance after {time} year/s: {total: .2f}frs")




while True: 
    principle = int(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle cant be less than or equal to zero")
    else:
        break

while True: 
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print("Interest rate cant be less than or equal to zero")
    else:
        break
    
while True: 
    time = int(input("Enter the time in years: "))
    if principle < 0:
        print("Time cant be less than or equal to zero")
    else:
        break
#formular to calculate compound interest
total = principle * pow((1 + rate / 100), time)

print(f"Balance after {time} year/s: {total: .2f}frs")