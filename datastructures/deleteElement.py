def removeElement(arr, val):
    n= len(arr)
    for i in range(n): 
        if (arr[i] == val): 
            
            break
    print(i)
    if (i < n): 
        print("yes")
        n = n - 1;
        print(n) 
        for j in range(i, n): 
            print("yesss")
            arr[j] = arr[j + 1]
            print(arr)
print(removeElement([1,2,3],3))