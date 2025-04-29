def bubble(arr,size):
    counter=1
    while(counter<size):
        for i in range(0,size-counter):
            if(arr[i]>arr[i+1]):
                temp=arr[i]
                arr[i]=arr[i+1]
                arr[i+1]=temp
        counter+=1
def selection(arr,size):
    for i in range(0,size-1):
        for j in range(i+1,size):
            if(arr[i]>arr[j]):
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
def binary(arr,size,targ):
    found=False
    start=0
    end=size-1
    while(not found and start<=end):
        mid=start+(end-start)/2
        if(targ>arr[mid]):
            start=mid+1
        elif(targ<arr[mid]):
            end=mid-1    
        else:
            found=True
            print("Your target is at index :{mid}")                                
size=int(input("Enter your size of array: "))
array=[0]*size
for i in range(0,size):
    array[i]=int(input("Enter your number for index: "))

print("\tYour array before sorting")
for i in range(0,size):
    print(f"Your number at index {i} :{array[i]}")
    
bubble(array, size)

print("\tYour array after sorting")
for i in range(0,size):
    print(f"Your number at index {i} :{array[i]}")        

target=int(input("Enter your target: "))

binary(array,size,target)