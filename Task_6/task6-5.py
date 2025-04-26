from shape import Circle, Rectangle, Triangle
c1 = Circle(7)
print(f"Radius of the circle: {c1.radius}")
print(f"Circle Area: {c1.area()}")
print(f"Circle Perimeter: {c1.perimeter()}")

r1 = Rectangle(5, 7)
print(f"Rectangle: Width = {r1.width}, Length = {r1.length}")
print(f"Rectangle Area: {r1.area()}")
print(f"Rectangle Perimeter: {r1.perimeter()}")

t1 = Triangle(5, 4, 4, 3, 5)
print(f"Triangle: Base = {t1.base}, Height = {t1.height}, Side1 = {t1.side1}, side2 = {t1.side2}, side3 = {t1.side3}")
print(f"Triangle Area: {t1.area()}")
print(f"Triangle Perimeter: {t1.perimeter()}")