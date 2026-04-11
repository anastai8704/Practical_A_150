# Practical 2 - Task 3
# Even Numbers Analysis (1–100)

even_numbers = [num for num in range(1, 101) if num % 2 == 0]

print("Even numbers between 1 and 100:")
print(even_numbers)

print("\nMinimum even number:", min(even_numbers))
print("Maximum even number:", max(even_numbers))
print("Total sum of even numbers:", sum(even_numbers))
