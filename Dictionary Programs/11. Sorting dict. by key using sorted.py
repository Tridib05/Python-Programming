# Initializing the key-value pairs
d = {2: 56, 100: 2, 3: 323}

print("Dictionary", d)

# Sorting key-value pairs by value, and by key if values are the same
sorted_items = sorted(d.items(), key=lambda kv: (kv[1], kv[0]))

print(sorted_items)
