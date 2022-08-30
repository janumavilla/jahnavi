n=int(input("Enter the value :"))
count=0
x=1
while (count<=n):
    sum=0
    for b in range(1,(x//2)+1):
        if (x%b==0):
            sum=sum+b
    if (sum==x):
        print(x,end=' ')
        count+=1
    x+=1
