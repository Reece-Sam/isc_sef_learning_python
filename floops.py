# for x in reversed(range(1, 11)):
#     print(x)

# print("HAPPY NEW YEAR!")

# for x in range(1, 11, 3):
#     print(x)


# credit_card = "2468-1357-9015-5107"

# for x in credit_card:
#     print(x)

# for x in range(1, 21):
#     if x == 13:
#         continue
#     else:
#         print(x)

# for x in range(1, 21):
#     if x == 17:
#         break
#     else:
#         print(x)








#MINI-PROJECT
#Creating a count down timer python

import time

my_time = int(input("Enter the time in seconds: "))

# for x in reversed(range(0, my_time)):
for x in range(my_time, 0, -1): 
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)


print("Time's Up!")
