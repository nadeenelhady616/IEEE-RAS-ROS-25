numbers = []
print("enter numbers and to stop enter -1")
while True:
    num = int(input())
    if num == -1:
        break
    else:
        numbers.append(num)
numbers.sort()
print(f"largest: {numbers[-1]} ,smallest: {numbers[0]}")
