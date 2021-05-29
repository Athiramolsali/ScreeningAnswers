
#Answer 2

def Range(list):
    largest = list[0]
    largest2 = None
    for item in list[1:]:
        if item > largest:
            largest2 = largest
            largest = item
        else:
            largest2 == None or largest2 < item
            largest2 = item

    print("Largest element is:", largest)
    print("Second Largest element is:", largest2)


list = [12, 45, 2, 41, 31, 10, 8, 6, 4]
Range(list)
