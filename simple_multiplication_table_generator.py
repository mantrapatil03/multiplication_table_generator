
print("Multiplication Table Generator")

try:
    number = int(input("Enter the number to generate table for: "))
    upto = int(input("Enter the range (e.g., 10 for 1 to 10): "))
except ValueError:
    print("Please enter valid integers.")
    exit()

if upto < 1:
    print("Range should be at least 1.")
    exit()

print(f"\nMultiplication Table for {number} (1 to {upto}):\n")

for i in range(1, upto + 1):
    print(f"{number} x {i} = {number * i}")

