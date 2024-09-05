# Write a program in which user def the no of element in array and
#  enter number you have to traverse the array and you have to sort array 
# bubble sort algorithm in python 
import array 
arr = array .array("i",[]) # taking input from user to set size of array 
n = int(input("enter array size: "))

#create a function to traverse array 
def PrintArray(arr):
    for i in range(0,n):
        print(arr[i] ,end=" -> ")

# bubble sort algorithms 
for i in range(0,n):
    num = int(input("enter a number : "))
    arr.append(num)
for j in range(0,n-1):
    for z in range(0,n-j-1):
        if arr[z]>arr[z+1]:
            temp = arr[z]
            arr[z] = arr[z+1]
            arr[z+1] = temp 

PrintArray(arr)