# Linear Search
my_list = [8, 9, 6, 3, 0, 7]
ITEM = 7

def search(list, item):
  for element in list:
    if element == item:
      return True
  return False

print(search(my_list, ITEM))