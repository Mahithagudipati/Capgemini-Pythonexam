def checkp(p):
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_chars = "!@#$%^&*(),.?\'':{}|<>"
    
    if len(p) < 8:
        return "Weak Password"
    
    for char in p:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True
    
    if has_upper and has_lower and has_digit and has_special:
        return "Strong Password"
    return "Weak Password"

def main():
    p = input("Enter the password : ")
    print(checkp(p))

main()