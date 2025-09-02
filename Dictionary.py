dict1 = {
    'Alice':89,
    'Mihir':99,
    "Subh":78,
    "Minakshi":88
}
name = input("Enter the student's name: ")
if name in dict1:
    x = dict1[name]
    print(f"{name}'s marks: ",x)
else:
    print("Student not found.")
