#bubble sort using while loop
def while_bubble_sort(lst):
  l = len(lst)-1
  sorted= False
  while not sorted:
    sorted=True
    for a in range(0,l):
      if lst[a]>lst[a+1]: # If first element is greater than second element
        sorted = False
        lst[a],lst[a+1]=lst[a+1] ,lst[a]
  return lst



import unittest
import random
def mergeSort(lst):
    length = len(lst)
    if length <= 1:
        return lst
    mid = length//2
    left = mergeSort(lst[:mid])
    right = mergeSort(lst[mid:])
    return merge(left, right)

def merge(left, right):
    leftIndex = 0
    rightIndex = 0
    result = []
    while leftIndex < len(left) and rightIndex< len(right):
        if left[leftIndex] < right[rightIndex]:
            result.append(left[leftIndex])
            leftIndex +=1
        else:
            result.append(right[rightIndex])
            rightIndex+=1
    print(left)
    result += left[leftIndex:]
    result += right[rightIndex:]
    return result

class test_mergeSort(unittest.TestCase):
    def test_mergeSort(self):
        random_list = [random.randrange(0, 1000) for _ in range(500)]
        print(random_list)
        self.assertEqual(mergeSort(random_list), sorted(random_list))

if __name__ == '__main__':
    unittest.main()

# print(mergeSort([5,4,3,4,6,8,1,2]))
