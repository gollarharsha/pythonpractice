lst = [1,10,1,-1, -1]
test={}
dupes=[]
# for ele in lst:
#     if ele not in test:
#         test[ele] = 1
#     else:
#         if test[ele] == 1:
#             dupes.append(ele)
#         test[ele] += 1



for ele in lst:
    test[ele] = test.get(ele,0)+1
    if  test[ele] > 1:
        dupes.append(ele)
print(dupes)
