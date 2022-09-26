new=int(input("Enter the number of new loaves purchased:"))
old=int(input("Enter the number of old loaves purchased:"))
rate_old=(185-(0.6*185))*old
rate_new=185*new
if(new<0):
    print("Enter a real number!")
else:
    print("Regular Price : Rs.185")
    print("Old loaves amount : Rs. ",rate_old)
    print("New loaves amount : Rs. ",rate_new)
    print("Total amount : Rs. ",rate_old+rate_new)
