'''use list as stack, array and queue'''
l = [3,4]
# as a stack
l.append(10)
l.pop()

# as a queue
l.insert(0, 5)
print(l)
l.pop()
print(l)