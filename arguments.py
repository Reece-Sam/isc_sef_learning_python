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
# def get_phone(country, area, first, last):
#     return f"{country}-{area}-{first}-{last}"

# phone_num = get_phone(country=237, area=67, first=560, last=3495)

# print(phone_num)

#=====================================================================
#Arbitrary Arguments

# def add(a, b):
#     return a + b 

# print(add(1, 2))

# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total

# print(add(1))

# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")

# display_name("Dr.", "Bonisam", "kelekoh", "Namme", "III")

#kwargs 
# def print_address(**kwargs):
#     # print(type(kwargs))   #dictionary
#     for key, value in kwargs.items():
#         print(f"{key}:{value}")

# print_address(street="Fomic-street", 
#               apt="207",
#               town="Buea" , 
#               division="Fako", 
#               zip="0000")
#===================================================================
#EXERCISE

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    # for value in kwargs.values():
    #     print(value, end=" ")
    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('town')} {kwargs.get('division')}, {kwargs.get('zip')}")

shipping_label("Dr.", "Bonisam", "longpants", "IV",
               street="Fomic-street",
               pobox="PO box 207",
               town="Buea" , 
               division="Fako", 
               zip="0000")
