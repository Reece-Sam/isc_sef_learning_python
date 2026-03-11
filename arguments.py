#Default Arguments
# def net_price(list_price, discount=0, tax=0.07):
#     return list_price * (1 - discount) * (1 + tax)

# print(net_price(15000, 0, 0.07))
#or
# print(net_price(15000))
# print(net_price(15000, 0.1))
# print(net_price(15000, 0.1, 0))

#===============================================================
#Exercise 
# import time

# def count(end, start=0):
#     for x in range(start, end+1):
#         print(x)
#         time.sleep(1)
#     print("DONE!")

# count(30, 15)
#================================================================

#Keyword Arguments
# def hello(greetings, title, first, last):
#     print(f"{greetings} {title}{first} {last}")

# hello("Hello", "Mr.", "Patrick", "star")


# for x in range(1, 11):
#     print(x, end=" ")

# print("1", "2", "3", "4", "5", "6", sep="-")

#===========================================================
#Exercise 
def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=237, area=67, first=560, last=3495)

print(phone_num)

#=====================================================================
#Arbitrary Arguments
