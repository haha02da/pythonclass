tel = {'jack': 4098, 'sape': 4139}

tel['guido'] = 4127

print(tel)

print(tel['jack'])
print(tel.get('irv'))  # 없으면 None

del tel['sape']
tel['irv'] = 4127
print(tel)


print(tel.get('nobody'))
print(tel.get('nobody', 0))
print(tel.get('nobody', '없음'))

if tel.get('nobody') is None:
    print("안전한 코드")

count = tel.get('nobody', 0)