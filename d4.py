# String Slicing and Indexin
text="sachin"
print(text[0])
print(text[1])
print(text[-1])
print(text[-2])#
#string[start:stop:step] .
x="Hello, Python}"
print(x[0:5])
print(x[:5])
print(x[7:])
print(x[::2])
print(x[-6:-1])
#Step Parameter
y="Python ,programming"
print(y[::2])
print(y[::-1])
# String Methods and Function
z="  hello world  "
print(z.upper())
print(text.lower())
print(text.title())
print(z.capitalize())
#Removing whitespace
print(z.strip())
print(z.lstrip())
print(z.rstrip())
#Finding and replacing text
r=" Python is fun"
print(r.find("is"))
print(r.replace("fun","awesome"))
#spliting and jiooninng 
s=" apple,banana,orange"
fruits=s.split(",")
print(fruits)
new_text="-".join(fruits)
print(new_text)
#formatting 
pi = 3.14159265
print(f"Pi rounded to 2 decimal places: {pi:.2f}")
#padding and alignment 
text = "Python"
print(f"{text:>10}")  # Right align
print(f"{text:<10}")  # Left align
print(f"{text:^10}")  # Center align
print("Hello\nWorld")   # \n → new line
print("Hello\tWorld")   # \t → tab space
print("She said: \"Hi\"")  # \" → double quote inside string
print('It\'s fine')     # \' → single quote inside string
print("C:\\Users\\Sachin") # \\ → backslash
#raw string
print("C:\newfolder")   # \n becomes newline (unexpected)
print(r"C:\newfolder")  # Raw string, \n is not special
# string encoding and decoding 
text = "Python "

# Encode to UTF-8 (default encoding)
encoded = text.encode("utf-8")
print(encoded)   # b'Python \xf0\x9f\x90\x8d'

# Decode back to string
decoded = encoded.decode("utf-8")
print(decoded)   # Python 
 #functions and modules
def greet(name):
    print(f"hello,{name}")

greet("Devidatta Mishra")
#Lambda functions 
square =lambda x:x*x
print(square(4))
#examples
numbers=[1,2,3,45,56]
sq=list(map(lambda x:x**2,numbers))
print(sq)
#recursion in pythons
def  factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
print(factorial(5))
#using global variaable 
x=10
def modify_global():
    global x
    x=5

modify_global()
print(x)
#Docstring - writing Function Doumentation
def add(a,b):
    """
    Returns the sum of two numbers.
    Parameters:
    a (int): The first number.
    b (int): The second number.
    Returns:
    int: The sum of the two numbers.
    """
 
    return a+b
print(add.__doc__)