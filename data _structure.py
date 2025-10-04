#list

mixed=[1,"sachin","wecant",56]
print(mixed)
print(type(mixed[2]))
#list methods
marks=[54,23,4,5,45,6,67]
marks.append(3)
print(marks)
marks.reverse()
print(marks)
print(marks.pop())
marks.remove(5)
print(marks)
marks.insert(3,78)
print(marks)
marks.sort()
print(marks)
# create a list containing the table of f
a=5
table=[]
for i in range(1,11):
    table.append(5*i)
print(table)
#list comphrehesion 
table1=[5*i for i in range(1,11)]
print(table1)
evens = [x for x in range(10) if x % 2 == 0]
print(evens)
colors = ['red', 'blue']
objects = ['ball', 'pen']
combinations = [c + ' ' + o for c in colors for o in objects]
print(combinations)
def square(x):
    return x*x

squares = [square(x) for x in range(5)]
print(squares)
###### tuple  ########
a=(1,2,3,4,5,6,7,8)
print(a)
print(a[2])
b=(2,)#tuple always need a comma if it is a single elelment

#######  set ######
s= {2,3,4,5}
print(s,type(s))
my_set = {1, 2, 3, 4}
my_set.add(5)
print(my_set)
my_set.remove(2)
print(my_set)
my_set.discard(10) # No error if element not found
print(my_set)
my_set.pop()
print(my_set)