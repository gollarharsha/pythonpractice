def removeDuplicates(listofElements):
    
    # Create an empty list to store unique elements
    uniqueList = []
    
    # Iterate over the original list and for each element
    # add it to uniqueList, if its not already there.
    for elem in listofElements:
        if elem not in uniqueList:
            uniqueList.append(elem)
    
    # Return the list of unique elements        
    return uniqueList


def remove_duplicates_space(arr):
    n=len(arr) #Length of an array
    if(n==0 or n == 1):
        return arr
    temp= [0]*n # Creating a list of elements
    pivot=0 # Initializing an index to 0
    for i in range(0, n-1): 
        if(arr[i]!=arr[i+1]):
            temp[pivot]=arr[i] #Replacing the elements in temp
            pivot=pivot+1 #Increasing index
            print(temp)
    temp[pivot]=arr[n-1]
    print(temp[0:pivot+1])



print(remove_duplicates_space([1,1,3,1,1]))




