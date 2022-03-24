import math
import random

def binarySearch(arr, target):
    arr.sort()

    left = 0
    right = len(arr)

    while left <= right:
        mid = math.floor((left + right) / 2)

        if target > arr[mid]:
            left = mid + 1
        elif target < arr[mid]:
            right = mid - 1
        else:
            return (arr.index(target)+1)

enter = True
myList = []
print("ENTER THE ELEMENTS OF THE LIST: ")
print("(enter -1 once done)")
while enter:
    ele = int(input())
    if ele != -1:
        myList.append(ele)
    else:
        enter = False
        
print("LIST: ",myList)
        
key = int(input("ENTER THE KEY: "))
print("Element found at", binarySearch(myList, key))
