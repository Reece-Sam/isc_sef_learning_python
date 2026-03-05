# name = input("Enter your full name: ")
# phone_number = input("Enter your phone #: ")

#length of a string
# result = len(name)
# result = name.find("m")
# result = name.rfind('r')
# name = name.capitalize()
# name = name.upper()
# name = name.lower()
# result = name.isdigit()
# result = phone_number.count("-")
# phone_number = phone_number.replace("-", "")

# print(phone_number)




# ====EXCERCISE====
#Validate user input exercise 
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

#Task 1
username = input("Enter a username: ")

if len(username) > 12:
    print("Your username cant be more than 12 characters")
    
#Task 2
elif not username.find(" ") == -1:
    print("Your username has spaces")
#Task 3
elif not username.isalpha():
    print("You username cant contain numbers")

else: 
    print(f"Welcome {username}")



