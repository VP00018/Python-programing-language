# **kwargs = allows you to pass multiple keyword-arguments
"""
def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street = "402 tulsi st.",
              
              apt = "06",
              city = "Nagpur",
              state = "MH",
              zip = "441904")

"""
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('apt')}, {kwargs.get('city')}, {kwargs.get('state')}, {kwargs.get('zip')}")
   
shipping_label("Dr.","Varad","Pandharkar","III",
               street = "402 tulsi st.",
               apt = "100",
               city = "nagpur",
               state = "MH",
               zip = "441904")