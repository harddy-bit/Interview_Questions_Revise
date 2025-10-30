# a = ["M","na","i","par", "xyz"]
# b = ["y","me","s","th"]
# output = ['My', 'name', 'is', 'parth', 'xyz']


a = ["M", "na", "i", "par", "xyz"]
b = ["y", "me", "s", "th"]

## create result empty list and append the a[i] and b[i[























result = []
for i in range(len(a)):
  if i < len(b):
    result.append(a[i] + b[i])
  else:
    result.append(a[i])

print(result)
