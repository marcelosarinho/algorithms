def selection_sort(arr):
  newArr = []

  for i in range(len(arr)):
    low = search_low(arr)
    newArr.append(arr.pop(low))

  return newArr

def search_low(arr):
  low = arr[0]
  lowIndex = 0

  for i in range(1, len(arr)):
    if (arr[i] < low):
      low = arr[i]
      lowIndex = i

  return lowIndex