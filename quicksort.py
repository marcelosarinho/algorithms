def quicksort(arr):
  if len(arr) < 2:
    return arr

  pivot = arr[0]
  lowerThanPivot = [i for i in arr[1:] if i <= pivot]
  higherThanPivot = [i for i in arr[1:] if i > pivot]
  return quicksort(lowerThanPivot) + [pivot] + quicksort(higherThanPivot)

print(quicksort([10, 5, 2, 3]))
print(quicksort([1, 35, 22, 345]))
print(quicksort([1, 1, 3, 4, 10, 5, 2]))