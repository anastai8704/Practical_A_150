even_numbers = []

for i in range(1, 101):
    if i % 2 == 0:
        even_numbers.append(i)

print("Even Numbers from 1 to 100:")
print(even_numbers)

print("\nMinimum Even Number:", min(even_numbers))
print("Maximum Even Number:", max(even_numbers))
print("Sum of Even Numbers:", sum(even_numbers))

# -----------------------------------
# 3. Even Numbers Analysis (1–50)
# -----------------------------------
even_numbers = [n for n in range(1, 51) if n % 2 == 0]

print("Even numbers between 1 and 50:")
print(even_numbers)

# three minimum even numbers
min_three = even_numbers[:3]
print("\nThree minimum even numbers:", min_three)

# three maximum even numbers
max_three = even_numbers[-3:]
print("Three maximum even numbers:", max_three)

# average
average = sum(even_numbers) / len(even_numbers)
print("Average of even numbers:", average)
