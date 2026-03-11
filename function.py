#FUNCTIONS
# def happy_birthday(name, age):
#     print(f"Happy birthday to {name} !")
#     print(f"You are {age} years old!")
#     print("Happy birthday to you!")
#     print()

# happy_birthday("Bonisam", 24)
# happy_birthday("Serena", 16)
# happy_birthday("Mesmerize", 23)

#======================================================
#Another Example

# def display_invoice(username, amount, due_date):
#     print(f"Hello {username}")
#     print(f"Your bill of {amount:.2f}frs is due: {due_date}")

# display_invoice("Bonisam", 1500, "03/04")
#=======================================================

#RETURN

# def add (x, y):
#     z = x + y
#     return z

# def subtract (x, y):
#     z = x - y
#     return z

# def multiply (x, y):
#     z = x * y
#     return z

# def divide (x, y):
#     z = x / y
#     return z

# print(add(14))
# print(subtract(2))
# print(multiply(48))
# print(divide(1.3333))

#=====================================
#Another example
def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last 

full_name = create_name("bonisam", "kelekoh")

print(full_name)