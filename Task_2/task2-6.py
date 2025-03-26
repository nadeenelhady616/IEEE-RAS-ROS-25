num = int(input("enter a number:"))
sum = 0
for i in range(2,num+1,2):
   sum += i
print(f"the sum of even numbers from 1 to {num} is {sum}")
