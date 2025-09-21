#looping
 #What are For Loops?
 #•For loops are used to iterate over a sequence (e.g., list, string, range)
fruits=["apple","orange"," cherry"]
for fruit in fruits :
    print(fruit)
# using range
#The range() function generates a sequence of numbers
for i in range(5):
    print(i)
#while loops
count=0
while count<5:
 print(count)
 count+=1
 #break
for i in range(5):
   if i==3:
      break
   print(i)
#continue
for i in range(5):
   if i==3:
      continue
   print(i)
#pass
for i in range(5):
   if i==3:
      pass
   print(i)
#        STRING IN PYTHON
a='hello ,python'
print(a)
b="hello,python"
print(b)
# triple - quated help to write multiple line
c=''' Strings are one of the most fundamental data types in Python. A string is a
 sequence of characters enclosed within either single quotes (
 ' ), double quotes
 (
 " ), or triple quotes (
 Creating Strings
'''
print(c)
#  STRING INDEXING
text=" hello world "
print(text[0])
print(text[1])
print(text[3])
#  STRING  SLICING
text1="Hello, python"
print(text1[0:5])
print(text1[:5])
print(text1[7:])
print(text1[::2])
#  STRING METHOD
print(text1.upper())
print(text.lower())
print(text.strip()) #strip() method is used to remove leading and trailing characters (by default spaces) from a string.
print(text.replace("world","python"))
name ="sachin"
age=25
print("my name is {} and iam {} years old.".format(name,age))
print(F"my name is {name} and I am {age} years old.")
message = '''
 Hello,
 This is a multi-line string example.
 Goodbye!
 '''
print(message)