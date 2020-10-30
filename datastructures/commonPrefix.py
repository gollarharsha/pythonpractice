
def splitList(lst):
    length = len(lst)
    if length <= 1:
        return lst
    mid = length//2
    left = splitList(lst[:mid])
    right = splitList(lst[mid:])
    return commonPrefix(left[0], right[0])

# def commonPrefix(left, right):
#     LeftLen = len(left)
#     RightLen = len(right)
#     i,j=0,0
#     sampleStr=""
#     while i<=LeftLen-1 and j <=RightLen-1:
#         if left[i] != right[j]:
#             break
#         sampleStr += left[i]
#         i+=1
#     return sampleStr

def commonPrefix(left, right):
    minLen = min(len(left), len(right))
    i=0
    sampleStr=""
    while i<=minLen-1 :
        if left[i] != right[i]:
            break
        sampleStr += left[i]
        i+=1
    return [sampleStr]

print(splitList(["flower", "flow", "flight"]))