# Practical 2 - Task 2
# Reverse Full Pyramid Pattern

# Practical 8 - Dynamic Reverse Pyramid

symbol = input("Enter symbol: ")
rows = int(input("Enter number of rows: "))

for i in range(rows, 0, -1):
    for j in range(i):
        print(symbol, end=" ")
    print()
