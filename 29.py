print("PASSWORD POLICY VALIDATION")

password = input("Enter your password: ")

errors = []

if len(password) < 8:
    errors.append("Minimum 8 characters required")

upper = False
lower = False
digit = False
special = False

for ch in password:
    if ch.isupper():
        upper = True

    elif ch.islower():
        lower = True

    elif ch.isdigit():
        digit = True

    else:
        special = True

if not upper:
    errors.append("At least one uppercase letter required")

if not lower:
    errors.append("At least one lowercase letter required")

if not digit:
    errors.append("At least one digit required")

if not special:
    errors.append("At least one special character required")

if len(password) != len(set(password)):
    errors.append("Repeated characters are not allowed")

if len(errors) == 0:
    print("\nPassword is VALID")
    print("Strong Password")
else:
    print("\nPassword is INVALID")

    for error in errors:
        print("-", error)
