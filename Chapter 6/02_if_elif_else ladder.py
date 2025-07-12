
a = int(input("Enter your age: "))

#If elif else ladder 

if(a>=18):
    print("Your are above the age of consent")

elif(a<0):
    print("You are entering an invalid age ")

elif(a==0):
    print("You are entering 0 which is not a valid age")

else:
    print("Your are below the age of consent")