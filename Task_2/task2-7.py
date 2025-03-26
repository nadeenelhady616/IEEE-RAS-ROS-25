num = int(input("enter a number: "))
prime_factors = []
if num % 2 == 0:
    prime_factors.append(2)
    while num % 2 == 0:
        num //= 2

i = 3
while i * i <= num:
    if num % i == 0:
        prime_factors.append(i)
        while num % i == 0:
            num //= i
    i += 2

if num > 2:
    prime_factors.append(num)
print("Prime Factors:", ', '.join(map(str, prime_factors)))
