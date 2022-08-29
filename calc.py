def add(x,y):
    return x+y
def subract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
print("select operation")
print('a.add')
print('b.subract')
print('c.multiply')
print('d.divide')
choice=input("enter the choice(a/b/c/d):")
num_1=int(input("enter the first number:"))
num_2=int(input("enter the second number:"))
if choice=='a':
    print(num_1,"+",num_2,"=",add(num_1,num_2))
elif choice=='b':
    print(num_1,"-",num_2,"=",subract(num_1,num_2))
elif choice=='c':
    print(num_1,"*",num_2,"=",multiply(num_1,num_2))
elif choice=='d':
    print(num_1,"/",num_2,"=",divide(num_1,num_2))
else:
    print("This is an invalid input")
                                    
