def compare(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0


# test compare function using predefined values from assignment table

print("test a > b: a = 5, b = 2")
result = compare(5, 2)
print(result)

print("test a < b: a = 2, b = 5")
result = compare(2, 5)
print(result)

print("test a == b: a = 3, b = 3")
result = compare(3, 3)
print(result)