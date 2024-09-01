import re

def checker(password):
    length = len(password) >= 8
    uppercase = bool(re.search(r'[A-Z]',password))
    lowercase = bool(re.search(r'[a-z]',password))
    digit = bool(re.search(r'[0-9]',password))
    specialchar = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    
    if length and uppercase and lowercase and digit and specialchar:
        return "Strong Password"
    else:
        feedback = "Weak Password \n"
        if not length:
            feedback = feedback + "Password length is less than 8 \n"
        if not uppercase:
            feedback = feedback + "Password does not contain the uppercase \n"
        if not lowercase:
            feedback = feedback + "Password does not contain the lowercase \n"
        if not digit:
            feedback = feedback + "Password does not contain the digit \n"
        if not specialchar:
            feedback = feedback + "Password does not contain the special character \n"
        return feedback

def main():
    Password = input("Enter the password: ")
    result = checker(Password)
    print(result)

if __name__ == "__main__":
    main()