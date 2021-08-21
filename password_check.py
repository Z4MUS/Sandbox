MIN_PASSWORD_LENGTH = 10

password = input("What is the password you would like to set? ")
while len(password) < MIN_PASSWORD_LENGTH:
    print(f"that password is too short, please enter a password of {MIN_PASSWORD_LENGTH} characters or more.")
    password = input("What is the password you would like to set? ")
print("*" * len(password))
