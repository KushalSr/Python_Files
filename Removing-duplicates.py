numbers = [1, 2, 2, 4, 4, 2, 12, 1, 3, 4, 8, 9, 0, 3]
uniques = []

for elements in numbers:
    if elements not in uniques:
        uniques.append(elements)
print(uniques)

uniques.sort()
print(f"Elements in ascending order: {uniques}")

