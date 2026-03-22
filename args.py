# *args = allows you to pass multiple non key argument

def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name ("Dr", "Varad", "Vivek", "Pandharkar", "III")
    