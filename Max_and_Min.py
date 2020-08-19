smallest = largest = None

while True:
    inp = input("Enter a number: ")
    if inp == "done":
        break

    try:
        num = int(inp)

    except:
        print("Invalid input")
        continue

    if smallest is None:
        smallest = num
    if largest is None:
        largest = num
    if num > largest:
        largest = num
    elif num < smallest:
        smallest = num

# def done(largest, smallest):
print("Maximum is", largest)
print("Minimum is", smallest)






