def selection(arr, rows, columns):
    for i in range(0,rows):
        for j in range(0,columns):
            for k in range(0, rows):
                for l in range(0,columns):
                    if(arr[k][l]>arr[i][j]):
                        temp=arr[k][l]
                        arr[k][l]=arr[i][j]
                        arr[i][j]=temp
def bubble(arr, rows, columns):
    counter=1
    total_elements=rows*columns
    while(counter<total_elements):
        for i in range(0, total_elements-counter):
            row=i//columns
            column=i%columns
            row1=i//columns
            column1=i%columns
            if(arr[row][column]>arr[row1][column1]):
                temp=arr[row][column]
                arr[row][column]=arr[row1][column1]
                arr[row1][column1]=temp
def binary(arr, rows, columns, targ):
    start=0
    end=rows*columns-1
    found=False
    while(not found and start<=end):
        mid=start+(end-start)//2
        row=mid//columns
        column=mid%columns
        if(targ>arr[row][column]):
            start=mid+1
        elif(targ<arr[row][column]):
            end=mid-1
        else:
            found=True
            print(f"Your target is at index: {row} {column}")                                                
rows=int(input("Enter the number of rows: "))
columns=int(input("Enter the number of columns: "))
array = [[0] * columns for _ in range(rows)] #SEE HOW TO DECLARE A 2D ARRAY IN PYTHON
for i in range(0,rows):
    for j in range(0, columns):
        array[i][j]=int(input(f"Enter the value for row: {i} and column: {j}= "))
print("\tBefore Sorting:") 
for i in range(0,rows):
    for j in range(0,columns):
        print(f"{array[i][j]} " ,end='') #Printing syntax for 2d array
    print()
  
selection(array, rows, columns)
        
print("\tAfter Sorting:") 
for i in range(0,rows):
    for j in range(0,columns):
        print(f"{array[i][j]} " ,end='') #Printing syntax for 2d array
    print()    
    
target=int(input("Enter your target: "))

binary(array, rows, columns, target)               