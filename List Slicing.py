list1 = []
for i in range(1,11):
    list1.append(i)
print("Original list: ",list1)
x = list1[0:6]
print("Extracted first five elements: ",x)
y= x.reverse()
print("Reversed extracted elements: ",y)