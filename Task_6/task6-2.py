from person import Person
from datetime import datetime
person_1 = Person("Nadeen Elhady", "Egypt", "2005-03-28")
print("Person_one:")
print(f"Name: {person_1.name}")
print(f"Country: {person_1.country}")
print(f"Date of Birth: {person_1.date_of_birth.strftime('%Y-%m-%d')}")
print(f"Age: {person_1.age()}")