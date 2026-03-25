<<<<<<< HEAD
unit = input("Is this Temperature in Celsius or Fahrenheit (C / F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round ((9 * temp) / 5 + 32 , 1)
    print(f"The temperature in Fahrenheit is : {temp} degree F")
elif unit =="F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Celsius is : {temp} degree C")

else:
=======
unit = input("Is this Temperature in Celsius or Fahrenheit (C / F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round ((9 * temp) / 5 + 32 , 1)
    print(f"The temperature in Fahrenheit is : {temp} degree F")
elif unit =="F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Celsius is : {temp} degree C")

else:
>>>>>>> c221da442758ed131598f2b393070929f837904f
    print(f"INVALID MEASUREMENT")