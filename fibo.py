n=int(input("Enter the number of terms in fibonacci series"))
a,b=0,1
s=a+b
print(a,b,end=" ")
for i in range(n-2):
    print(a+b,end=" ")
    a,b=b,a+b
    s=s+b
print()
print("Sum of",n,"terms of series =",s)
