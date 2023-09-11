x = "dfdfdgdfgfgg"
print(x[::-1])

x= set()
print(type(x))

x= [1,2,3,4,5]
print(x)
print(*x)

def func(x,y):
    print(x,y)

# * unpacks a data type like list 
pairs = [(1,2), (3,4)]
for pair in pairs:
    func(*pair)
    
#to unpack a dict you need **
func(**{"x":1, "y":2})
    
# Python has *args, which allows us to pass a variable number of non-keyword arguments to a function. Non-keyword here means that the arguments should not be a dictionary (key-value pair), and they can be numbers or strings.
#*args enable us to pass the variable number of non-keyword arguments to functions, but we cannot use this to pass keyword arguments. Keyword arguments mean that they contain a key-value pair, like a Python dictionary.
#**kwargs allows us to pass any number of keyword arguments.
def funcy(*args, **kwargs):
    print(args, kwargs)
    
funcy(1,2,3,4,5, "hello", one=1, two=2)
    
    