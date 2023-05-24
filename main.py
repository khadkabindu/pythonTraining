def check_odd_even(number):
    if number % 2 == 1:
        print("odd")
    elif number == 0:
        print("Zero")
    else:
        print("even")


check_odd_even(10)


myList = [1, 2, 3, 4, 2, 45]
for element in myList:
    print(element)

for index, element in enumerate(myList):
    print(element+index)


