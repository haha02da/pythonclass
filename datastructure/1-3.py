a = [1,2,3,2,4]
a.remove(2)# 첫 번째 2만 제거
print(a)

last = a.pop()# 마지막 꺼내기
print(f"pop: {last} => {a}")

second = a.pop(1)# 인덱스 1 꺼내기
print("pop(1):", second,"=>", a)

a.remove(99)# 첫 번째 2만 제거
a.clear()
print(a)

