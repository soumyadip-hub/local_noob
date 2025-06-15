# --------at first we learn about decoraters-----
# decorator is a function that takes a function,it creates a new function inside its body (wrapper). Then it returns that new function

def decorator(func):
    def wrapper():
        print("iam about to execute a function...")
        func()
        print("i have executed this function")
    return wrapper

@decorator

def say_hello():
    print("Hello!")

say_hello()

# f = decorator(say_hello)              
# f()
 # insipite of using this sheddy calling ----- use it



'''
f will something looks like this
def f():
    print("iam about to execute the code")
    print("Hello!")
    print("I have to execute this function")

'''

# --------------decorator using with arguments------

def repeat(n):
    def decorator(func):
        def wrapper(a):
            for i in range(n):
                func(a)
        return wrapper
    return decorator

@repeat(7)
def say_hello(a):
    print(f"hello ! {a}")


'''
def decorates(func):
    def wrapper(a):
        for i in range(n):
            say_hello(a)
    return wrapper

'''

say_hello("Eagle")


# ----------learn about geeters and setters------

