x = int(input("정수를 입력하세요: "))

if x < 0:
    print("음수입니다.")
elif x == 0:
    print("0입니다.")
elif x == 1:
    print("1입니다.")
else:
    print("2 이상입니다.")


if x % 2 == 0:
    print(f"{x}는 짝수입니다.")
else:
    print(f"{x}는 홀수입니다.")