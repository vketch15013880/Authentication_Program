##incomplete draft
def validatePassword(s):
    Cap = False
    Lower = False
    Digit = False
    
    
    for i in s:
        if i.isupper():
            Cap = True
        if i.islower():
            Lower = True
        if i.isdigit():
            Digit = True
     

    if Cap & Lower & Digit:
        return 'Valid'
    else:
        return 'Not valid'

p = input("Password: ")
print(validatePassword(p))

