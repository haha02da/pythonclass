a = ["Mary", "had", "a", "little", "lamb"]

for i in range(len(a)):
    print(i, a[i])

print("-"*20)

for i, item in enumerate(a,1):
    print(i, item)
