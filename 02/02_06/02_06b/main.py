# Tuples are immutable array-like structures

point = (5, 2)

x = point[0]
y = point[1]

def calculate_square_property(side_length):
  area = side_length * side_length
  perimeter = 4 * side_length
  return (area, perimeter)

result = calculate_square_property(5)
print(result)
print("Area: ", result[0])
print("Perimeter: ", result[1])