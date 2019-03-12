fruits = ["apple", "orange", "pear", "banana", "apple"]

print("rozpoczynam petle")

for i, fruit in enumerate(fruits):
    print("sprawdzam {}".format(i))
    if i == 3:
        break

    print("{} jest ok". format(fruit))

print("koniec")