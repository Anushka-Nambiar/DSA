def linearSearch(a, k):
    for i in range(len(a)):
        if a[i] == k:
            return (i+1)
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
print("Element found at", linearSearch(myList, key))
