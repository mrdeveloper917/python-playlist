# Methods in Dictionary:-
marks = {
    "Harry": 100,
    "Shubham": 56,
    "Rohan": 23
    }

print(marks.items()) #dict_items([('Harry', 100), ('Shubham', 56), ('Rohan', 23)])
print(marks.keys()) # dict_keys(['Harry', 'Shubham', 'Rohan'])
print(marks.values()) # dict_values([100, 56, 23])

marks.update({"Harry":98, "Renuka": 100})
print(marks) # {'Harry': 98, 'Shubham': 56, 'Rohan': 23, 'Renuka': 100}

print(marks.get("Harry2")) # prints none
print(marks["Harry2"]) # return an error