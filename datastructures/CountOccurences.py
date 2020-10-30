# def countOccur(testList):
#     sampleDict = {}
#     for element in testList:
#         sampleDict[element] = sampleDict.get(element,0)+1
#     return sampleDict


#Through Recursion

def countOccur(testList, key):
    if testList == []:
        return 0
    if testList[0] == key:
        return 1+countOccur(testList[1:], key)
    else:
        return 0+countOccur(testList[1:], key)

print(countOccur([0,1,1,1,2,3,3], 1))