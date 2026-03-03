import math 

x = 9.9

# print(math.pi)
# print(math.e)

#square-roots
# result = math.sqrt(x)

#ceil(rounds up the number)
# result = math.ceil(x)

#floor(rounds down)
# result = math.floor(x)

# print(result)



#Exercise 1: calculate the circumference of a circle 
# radius =  float(input("Enter the radius of a circle: "))

# circumference = 2 * math.pi * radius

# print(f"The circumference is: {round(circumference, 2)}")


# Exercise 2: Calculate the area
# radius = float(input("Enter the radius of the circle: "))

# area = math.pi * pow(radius, 2)

# print(f"The area of the circle is: {round(area, 2)}cm^2")



#Exercise3: Calculate the hypotenus
a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"side C = {c}")