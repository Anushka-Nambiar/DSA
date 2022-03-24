def linearSearch(k, a, index=0):
    if index >= len(a):
        return False
    if a[index] == k:
        return index
    else:
        return linearSearch(k, a, index+1)
    

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
print("Element found at", linearSearch(key,myList))
