def has_unique_characters(data):
    unique_len = set(data)
    return len(unique_len) == len(data)

print(has_unique_characters('sample'))
print(has_unique_characters('hello world'))
print(has_unique_characters('linkedin'))
print(has_unique_characters('python'))
