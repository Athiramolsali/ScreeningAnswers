#Answer1
list = []
n = int(input("Enter number of elements in list: "))

for i in range(1, n + 1):
    elements = int(input("Enter elements: "))
    list.append(elements)

print("Largest element is:", max(list))
