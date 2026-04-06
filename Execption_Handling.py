# Execption = An event that interrupts the flow of a program
# (ZeroDivisionError),(TypeError),(ValueError).  Ex= (1 / 0), (1 + "1"), (int("Pizza"))
# 1) .try
# 2) .except
# 3) .finally

try:
    number = int(input("Enter a number: "))
    print(1 / number)    # It gives ZeroDivisionError (If we do not apply .try)
except ZeroDivisionError:
    print("You can't divide by zero IDIOT!")

except ValueError:
    print("Enter Only numbers Please!")

except Exception:
    print("Something Went Wrong!")

finally:
    print("Do Some Cleanup Here")