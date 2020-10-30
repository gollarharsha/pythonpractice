def sorting(s):
    length = len(s)-1
    sorted= False
    while not sorted:
        sorted= True
        for i in range(length):
            print(s[i], s[i+1])
            if s[i][1] > s[i+1][1]:
                sorted= False
                s[i],s[i+1] = s[i+1],s[i]
                print(s)
                print()
    return s

print(sorting([(2, 5), (1, 2), (1,3),(1,1)]))


# def sorting(arr):
#   n = len(arr)
#   for i in range(0, n):
#     for j in range(0,n -i-1):
#       if arr[j] > arr[j+1] : 
#         arr[j], arr[j+1] = arr[j+1], arr[j]
#   return arr

# print(sorting([(2, 5), (1, 2), (1,3),(1,1)]))


