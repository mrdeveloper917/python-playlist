def inch_to_cms(inch):
    return inch * 2.54
n = int(input("Enter values in inch: "))
c = inch_to_cms
print(f"The corresponding value in cms is {c(n)}")