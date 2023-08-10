num = int(input())
cnt = []

for i in range(1,num+1):
    if num%i == 0:
        cnt.append(i)
if len(cnt) == 2:
    print("소수입니다.")

