array = [0] * 10
odd_sum = 0
even_sum = 0
for i in range(0, 10):
    array[i] = int(input(f"Enter Number {i + 1}: "))
for i in range(1, 10, 2):
    odd_sum=odd_sum+array[i]
for i in range(0, 10, 2):
    even_sum=even_sum+array[i]
print(f"Sum of odd indexes: {odd_sum}")
print(f"Sum of even indexes: {even_sum}")