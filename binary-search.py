def binary_search(items, item):
  low = 0
  high = len(items) - 1

  while low <= high:
    medium = (low + high) // 2
    attempt = items[medium]
    if (attempt == item):
      return medium
    if (attempt > item):
      high = medium - 1
    else:
      low = medium + 1
  return None

numbers = [1, 3, 5, 7, 9, 11]

print(binary_search(numbers, 3))
print(binary_search(numbers, -1))