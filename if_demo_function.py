def check(number):
    if number > 0:
        return "Positive"
    elif number == 0:
        return "Zero"
    else:
        return "Negative"
    
print(check(10))
print(check(-10))
print(check(0))
