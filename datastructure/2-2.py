from collections import deque

q = deque(["Eric","John","Michael"])
q.append("Terry")
q.append("Graham")
print(q)

print(q.popleft())
print(q.popleft())
print(q)

