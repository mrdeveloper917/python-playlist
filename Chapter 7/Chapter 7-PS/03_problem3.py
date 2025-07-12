n = int(input("Enter a number:"))

for i in range (1, 11):
    print(f"{n} X {i} = {n * i}")

''' Output:
Enter a number:7
7 X 1 = 7
7 X 2 = 14
7 X 3 = 21
7 X 4 = 28
7 X 5 = 35
7 X 6 = 42
7 X 7 = 49
7 X 8 = 56
7 X 9 = 63
7 X 10 = 70
'''

i = 1
while(i < 11):
    print(f"{n} X {i} = {n * i}")
    i += 1
''' Output:
Enter a number:7
7 X 1 = 7
7 X 2 = 14
7 X 3 = 21
7 X 4 = 28
7 X 5 = 35
7 X 6 = 42
7 X 7 = 49
7 X 8 = 56
7 X 9 = 63
7 X 10 = 70
'''