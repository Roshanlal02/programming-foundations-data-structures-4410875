card_stack = []

card_stack.append("Jacl of hearts")
card_stack.append("2 of diamonds")
card_stack.append("10 of spades")

top_card = card_stack.pop()
print(top_card)
top_card = card_stack[-1]
print(top_card)

if not card_stack:
  print("Card stack is empty")
else:
  print(len(card_stack))