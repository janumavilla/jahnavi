myList = [16,18,27,16,23,21,19]
print("Your List is : ", myList)
print("Prime numbers in your list is/are : ")
for num in myList:
 if num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            break
        else:
            print(num)
  
