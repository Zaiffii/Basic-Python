def reverse(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        # Swap elements
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


# Input size of array
size = int(input("Enter the size of the array: "))

# Input array elements
array = []
for i in range(size):
    num = int(input(f"Number {i + 1}: "))
    array.append(num)

# Display the array before reversing
print("\tBefore Swapping")
for i in range(size):
    print(f"Number {i + 1}: {array[i]}")

# Reverse the array
reverse(array)

# Display the array after reversing
print("\tAfter Swapping")
for i in range(size):
    print(f"Number {i + 1}: {array[i]}")
