"""
Deben Peterson
10/23/2019
Sort
"""

def quickSort(arr):
  if len(arr) <= 1:
    return arr
  new=[]
  pivot= arr[0]
  less=[]
  greater=[]
  same=[]
  for i in arr:
    if i > pivot:
      greater.append(i)
    elif i < pivot:
      less.append(i)
    else:
      same.append(i)
  less= quickSort(less)
  greater= quickSort(greater)
  new.extend(less)
  new.extend(same)
  new.extend(greater)
  return new

array = [12, 200, 45, 1, 57, 23]

print(quickSort(array))