#List
# fruits = ["apple", "orange", "banana", "grades"]
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("apple" in fruits)
 
# fruits[0] = "co2D key pad on a phoneconut"
# fruits.append("cocunut")
# fruits.remove("banana")
# fruits.insert(0, "coconut")
# fruits.sort()
# fruits.reverse()
# fruits.clear()

#return the index of apple 
# print(fruits.index("apple"))

# print(fruits.count("tomatoes"))

# print(fruits)
# for fruits in fruits:
#     print(fruits)


#SET
# fruits = {"apple", "orange", "banana", "coconut"} 
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("apple" in fruits)

# fruits.add("pineapple")
# fruits.remove("banana")
# fruits.pop()
# fruits.clear()

# print(fruits)

#TUPLE
# fruits = ("appls))
# print(help(fruits))
# print(len(fruits))
# print("apple" ie", "mango", "orange", "orange", "coconut")
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("pineapple" in fruits)

# print(fruits.index("apple"))
# print(fruits.count("orange"))

# print(fruits)
# for fruits in fruits:
#     print(fruits)


#Note: A tuple is faster than a list



#=====EXERCISE=====
# (Shopping cart program)

# foods = []
# prices = []
# total = 0s))
# print(help(fruits))
# print(len(fruits))
# print("apple" i

# while True:
#     food = input("Enter a food buy(q to quit): ")
#     if food.lower() == "q":
#         break 
#     else:
#         price = float(input(f"Enter the price of a {food}:  frs"))
#         foods.append(food)
#         prices.append(price)

# print("-----Your CART-----")

# for food in foods:
#     # print(food, end=" ")
#     print(food)

# for price in prices:
#     # total = total + price 
#     #     or 
#     total += price 

# print()
# print(f"Your total is: {total}frs")
#End of Exercise 


#Topic: 2D List
# fruits =        ["apple", "orange", "mangoes", "grape"]
# vegetables =    ["tomatoes", "carrots", "bruckly"]
# meats =         ["chicken", "goat-meat", "turkey", "pork"]

# groceries = [fruits, vegetables, meats]


# print(groceries[2][0])
# print(fruits)s))
# print(help(fruits))
# print(len(fruits))
# print("apple" i
           #or


# #A list inside a list
# groceries =  [["apple", "orange", "mangoes", "grape"],
#              ["tomatoes", "carrots", "bruckly"],
#              ["chicken", "goat-meat", "turkey", "pork"]]

# #A tuple made of sets
# groceries =  ({"apple", "orange", "mangoes", "grape"},
#              {"tomatoes", "carrots", "bruckly"},
#              {"chicken", "goat-meat", "turkey", "pork"})

# #A set made of list
# groceries =  {["apple", "orange", "mangoes", "grape"],
#              ["tomatoes", "carrots", "bruckly"],
#              ["chicken", "goat-meat", "turkey", "pork"]}

# for collection in groceries:
#     for food in collection:
#       print(food, end=" ")
#     print()


#====Exercise====
# 2D key pad on a phone

num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()
#End of Exercise 






