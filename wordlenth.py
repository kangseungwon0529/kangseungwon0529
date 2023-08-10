t = int(input())
for tc in range(1,t+1):
    str1 = input()
    str2 = input()

    result = 0
    for i in range(len(str1)):
        cnt = 0
        for j in range(len(str2)+1):
            if str1[i] == str2[i+j]:
                cnt += 1
            else:
                cnt = 0
        if cnt == len(str1):
            result += 1
    print(f"#{tc} {result}")