#prime number 
# Function to check prime number
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):  
        if num % i == 0:
            return False
    return True

# Example usage
n = int(input("Enter a number: "))
if is_prime(n):
    print(n, "is a Prime Number")
else:
    print(n, "is NOT a Prime Number")
#avrage number
# Take numbers from user
n = int(input("How many numbers? "))
numbers = []

for i in range(n):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Calculate average
average = sum(numbers) / len(numbers)
print("Average =", average)
 # nums = [1, 2, 3]
nums.append(4)   # add 4 at the end
print(nums)      # [1, 2, 3, 4]
