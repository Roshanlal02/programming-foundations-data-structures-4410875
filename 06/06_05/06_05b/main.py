from collections import deque

def check_matching_paranthesis(s):
  stack = deque()
  for char in s:
    if char == "(":
      stack.append(char)
    elif char == ")":
      if not stack:
        return False
      stack.pop()
    
  return len(stack) == 0

print(check_matching_paranthesis("()"))
print(check_matching_paranthesis("(hi there)"))
print(check_matching_paranthesis("(hell)o"))
print(check_matching_paranthesis("((hi there)) thi si a test"))

print(check_matching_paranthesis("()ok)"))
print(check_matching_paranthesis("(hi (there"))
print(check_matching_paranthesis("((hell)"))
print(check_matching_paranthesis(")hi there() thi si a test"))

