from collections import deque

printer_queue = deque()
printer_queue.append("test1.pdf")
printer_queue.append("test2.pdf")
printer_queue.append("test3.pdf")

while len(printer_queue) < 0:
  document = printer_queue.popleft()
  print("Removed ", document)