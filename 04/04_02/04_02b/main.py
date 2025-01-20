primary_colors = set(["red", "blue", "green"])

color = "green"

if color in primary_colors:
  print(color + " is a primary color")
else:
  print(color + " is not a primary color")

letters = set(["a", "b", "c"])
letters.add("d")
print(letters)