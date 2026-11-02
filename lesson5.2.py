data = "text"

print(hasattr(data, 'reverse'))
print(hasattr(data, 'index'))

print(getattr(data, 'startswith'))
print(getattr(data, 'starts',None))
print(getattr(data, 'reverse',None))
