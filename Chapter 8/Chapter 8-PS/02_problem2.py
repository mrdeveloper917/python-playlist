# c/5 = (f-32)/9
def f_to_c(f):
    return 5*(f-32)/9

f = int(input("Enter termperature in F: "))
c = f_to_c(f)
print(f"{round(c, 2)}")

'''Output:-
Enter termperature in F 100
37.78
'''