# Practical 2 - Task 1
# Right Half Pyramid Pattern

# Practical 8 - Dynamic Right Half Pyramid

symbol = input("Enter symbol: ")
rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    for j in range(i):
        print(symbol, end=" ")
    print()