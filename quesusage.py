from collections import deque

s = deque(["Pedro", "Linda"])
s.append("Melinda")
print(s)


s.append("Terry")
s.append("Silva")
s.append("Minda")
s.append("Jerry")


print(s)
s.popleft()


print(s)

s.pop()
print(s)
vec = [[1,2,3], [4,5,6], [7,8,9]]
#list comprehension
print([num for elem in vec for num in elem])


squares = [x**2 for x in range(10)]
print(squares)
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print(flat)

mult = lambda a, b: a * b

mult_result = mult(9, 9)
print(mult_result)

numbers = [1,2,3,4,5,6,7,8,9,10]
squares_lam = list(map(lambda x: x ** 2, numbers))
print(squares_lam)

even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)

even_squares = [(lambda x: x**2) (x) for x in numbers if x % 2 ==0]
print(even_squares)
even_squares = list((lambda x: x**2) (x) for x in numbers if x % 2 ==0)
print(even_squares)

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
