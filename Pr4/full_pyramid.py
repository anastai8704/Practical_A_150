# ==========================================
# FULL PYRAMID - SET A + SET B (Merged)
# ==========================================

#print("===== SET A : Alphabet Full Pyramid =====\n")

rows = 5

# Alphabet Pyramid (Increasing)
for i in range(1, rows + 1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()

#print("\n")

#print("===== SET B : Star Full Pyramid (Inverted) =====\n")

# Star Pyramid (Decreasing)
for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
