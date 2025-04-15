import re

def validateCard(cardNum):
    pattern = r"^([456]\d{3})-?(\d{4})-?(\d{4})-?(\d{4})$"
    consecutive_repeated_digits = r"(?!.*(\d)\1{3,})"
    
    if re.match(pattern, cardNum) and re.match(consecutive_repeated_digits, cardNum.replace("-", "")):
        return "Valid"
    else:
        return "Invalid"
    
if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        card = input().strip()
        print(validateCard(card))