weight = float(input("Enter your weight: "))
unit = input("Kilogram or Pounds ? (K or P): ")

if unit == "K":
    weight = weight * 2.205
    unit = "LBS."
    print(f"Your weight is: {round(weight, 3)} {unit}")

elif unit == "P":
    weight = weight / 2.205
    unit = "KGS."
    print(f"Your weight is: {round(weight, 3)} {unit}")
    
else:
    print(f"{unit} was not valid")
