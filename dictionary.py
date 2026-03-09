capitals = {"Cameroon": "Yaounde",
            "Nigeria": "Abuja",
            "Canada": "Toronto",
            "England": "London"}

#gets the attributes
# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("Cameroon"))

# if capitals.get("Senegal"):
#    itals.clear()


# keys = capitals.keys()
# for key in capitals.keys():
#     print(key)

# values = capitals.values()
# for value in capitals.values():
#  print(value)

# items = capitals.items() print("That capital exists")
# else:
#     print("That capital doesnt exists")

# capitals.update({"Germany": "Berlin"})
# capitals.update({"Cameroon": "Buea"})
# capitals.pop("Germany")
# capitals.popitem()
# capitals.clear()


# keys = capitals.keys()
# for key in capitals.keys():
#     print(key)

# values = capitals.values()
# for value in capitals.values():
#  print(value)

# items = capitals.items()
# for key, value in capitals.items(): 
#   print(f"{key}: {value}")


#====Exercise==== 
#A Concession stand program
menu = {"pizza": 6000,
        "popcorn": 1000,
        "sharwama":1000,
        "chips": 100,
        "meat-pies": 2000,
        "soda": 600,
        "beer": 1000 }

cart = []
total = 0


print("------- MENU -------")
for key, value in menu.items():
    print(f"{key:10}: {value:.2f}frs")
print("----------------")

while True: 
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("--------- YOUR ORDER --------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Total is: {total:.2f}frs")