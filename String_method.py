"""

# name = input("Enter your full name: ")

# phone_number = input("Enter your phone #: ")

# result = len(name)

# result1 = name.find("d")

# result2 = name.rfind("r")

# name = name.capitalize()\

# name = name.upper()

# name = name.lower()

# result3 = name.isdigit()

# result4 = name.isalpha()

# result = phone_number.count("-")

print(result)

"""

# Validate user input exercise
# 1) username is no more than 12 characters
# 2) username must not contain spaces 
# 3) username must not contain digit

username = input("Enter a username: ")
#username.find(" ")

if len(username) > 12:
    print("your username can't be more than 12 characters")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("Your username can't contain numbers")
else:
    print(f"Welcome {username}")
