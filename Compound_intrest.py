<<<<<<< HEAD
principal = 0
rate = 0
time = 0

while principal <= 0:
    principal = float(input("Enter the principal amount: "))
    if principal <= 0:
        print("principal can't be less than or equal to zero") 

while rate <= 0:
    rate = float(input("Enter the Intrest Rate: "))
    if rate <= 0:
        print("Intrest Rate can't be less than or equal to zero") 

while time <= 0:
    time = int(input("Enter the time in years: "))
    if time <= 0:
        print("Time can't be less than or equal to zero") \
        
total = principal * pow((1 + rate / 100), time)

=======
principal = 0
rate = 0
time = 0

while principal <= 0:
    principal = float(input("Enter the principal amount: "))
    if principal <= 0:
        print("principal can't be less than or equal to zero") 

while rate <= 0:
    rate = float(input("Enter the Intrest Rate: "))
    if rate <= 0:
        print("Intrest Rate can't be less than or equal to zero") 

while time <= 0:
    time = int(input("Enter the time in years: "))
    if time <= 0:
        print("Time can't be less than or equal to zero") \
        
total = principal * pow((1 + rate / 100), time)

>>>>>>> c221da442758ed131598f2b393070929f837904f
print(f"Balance after {time} year/s: ${total:.2f}")