a = ["Mary", "had", "a", "little", "lamb"]

for i in range(len(a)):
    print(i, a[i])

for i, item in enumerate(a,2):
    print(i, item)
