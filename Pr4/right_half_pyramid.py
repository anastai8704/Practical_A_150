
rows = 6

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()

# -----------------------------------
# 1. Inverted Right Half Pyramid
# -----------------------------------
rows = 5
numbers = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6]  # sequence as per pattern
index = 0

for i in range(rows, 0, -1):
    for j in range(i):
        print(numbers[index], end=" ")
        index += 1
    print()
