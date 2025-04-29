# Given array
myArray = [3, 6, 7, 9, 3, 6, 8, 3, 5, 10]
seen = set()  # Set to track seen numbers

# Process the array to remove duplicates
for i in range(len(myArray)):
    if myArray[i] in seen:
        myArray[i] = 0  # Replace duplicate with 0
    else:
        seen.add(myArray[i])  # Mark as seen

# Display the updated array
print("Array after removing duplicates:", myArray)
