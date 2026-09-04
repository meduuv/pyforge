from pyforge import chunks, clamp, flatten

print(clamp(120, 0, 100))
print(list(chunks([1, 2, 3, 4, 5], 2)))
print(flatten([[1, 2], [3], [4, 5]]))
