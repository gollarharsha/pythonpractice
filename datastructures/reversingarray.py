def reversingArray(array):
    if len(array) == 0:
        return []
    elif len(array) == 1:
        return array
    return [array[len(array)-1]] + reversingArray(array[:len(array)-1])

print(reversingArray([1,2,4]))

#Using stack

def reversingStack(x, y=None):
    if y is None:
        y=[]
    y.append(x.pop())
    if x:
        reversingStack(x,y)
    return y
    
print(reversingStack([1,2,3]))