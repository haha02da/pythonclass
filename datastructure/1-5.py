numbers = [3,1,4,1,5,9,2]

a = numbers.copy()
a.sort()
print("sorted:", a)

b = numbers.copy()
b.sort(reverse=True)
print("desc:", b)

c = numbers.copy()
c.reverse()
print("reversed:", c)
print(numbers)
