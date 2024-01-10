def simple_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@simple_decorator
def hello():
    print("Hello, world!")

hello()

from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper function"""
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    """Greet someone."""
    print(f"Hello {name}!")

say_hello("Alice")
print(say_hello.__name__)
print(say_hello.__doc__)
