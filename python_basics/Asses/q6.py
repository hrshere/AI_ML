items = ['milk', 'tea', 'coffee','sugar', 'cream']
# latte = items[:1] + items[2:4]
# latte = [item for item in items if item != "tea" and item != "cream"]
latte = items[::2]
print(latte)