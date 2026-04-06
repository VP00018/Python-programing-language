# Decorator = A function that extends the behaviour of another function w/o modifying the base function.

def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("*You add sprinkles 🎊*")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("*You add fudge choice 🍫*")
        func(*args, **kwargs)
    return wrapper

@add_sprinkles
@add_fudge

def get_ice_cream(flavor):
    print(f"Here is your {flavor} Ice cream 🍨")

get_ice_cream("Chocolate")
