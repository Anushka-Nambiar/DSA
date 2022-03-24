def binarySearch(arr, start, end, x):
    if end >= start:
        mid = start + (end- start)//2
        if arr[mid] == x:
            return (mid+1)
        elif arr[mid] > x:
            return binarySearchAppr(arr, start, mid-1, x)
        else:
            return binarySearchAppr(arr, mid+1, end, x)
    else:
        return -1
    
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
print("Element found at", binarySearch(myList, 0, len(myList)-1, key))
