print("Enter a number:")
while True:
    num = input()
    if num.isdigit(): #checks if input contains digits only
        break
    else:
        print("That wasn't a number, try again.")
