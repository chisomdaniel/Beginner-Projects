# find the base of a triangle given its area and height

area = float(input("Enter the area: "))
height = float(input("Enter the height: "))

base = (2 * area) / height

print("The base of the triangle is " + str(base))
