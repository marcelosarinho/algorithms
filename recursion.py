def factorial(num):
  if num == 1:
    return 1
  else:
    return num * factorial(num - 1)
  
print(factorial(3))
print(factorial(1))

def sum(arr):
  if arr == []:
    return 0
  
  return arr[0] + sum(arr[1:])
  
print(sum([1, 2, 3, 4]))
print(sum([10]))
print(sum([]))

def count_itens(itens):
  if itens == []:
    return 0
  
  return 1 + count_itens(itens[1:])

print(sum([1, 2, 3, 4]))
print(sum([10]))
print(sum([]))

def highest_value(list):
  if len(list) == 2:
    return list[0] if list[0] > list[1] else list[1]
  
  highest = highest_value(list[1:])
  return list[0] if list[0] > highest else highest

print(highest_value([1, 2, 3]))
print(highest_value([8, 5, 3, 2]))
print(highest_value([45, 2]))