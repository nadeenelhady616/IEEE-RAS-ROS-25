from circle import Circle
rad = int(input("Input the radius of the circle:"))
circle1 = Circle(rad)
print(f"Area of the circle: {circle1.area()}")
print(f"Perimeter of the circle: {circle1.perimeter()}")