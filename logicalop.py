temp = 45
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is canceled")
else:
    print("The outdoor event is still active")

#and 
temp = 20
is_sunny = True 

if temp >= 28 and is_sunny:
    print("It is HOT outside 🥵")
    print("It is SUNNY ☀️") 
elif temp <= 0 and is_sunny:
    print("It is COLD outside 🥶")
    print("It is SUNNY ☀️") 
elif  28 > temp > 0 and is_sunny:
    print("It is WARM outside 😀")
    print("It is SUNNY ☀️") 

#not
temp = 0
is_sunny = False 

if temp >= 28 and not is_sunny:
    print("It is HOT outside 🥵")
    print("It is CLOUDY ☁️") 
elif temp <= 0 and not is_sunny:
    print("It is COLD outside 🥶")
    print("It is CLOUDY ☁️") 
elif  28 > temp > 0 and not is_sunny:
    print("It is WARM outside 😀")
    print("It is CLOUDY ☁️") 


