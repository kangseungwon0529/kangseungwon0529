t = 10
for tc in range(1,t+1):
    size, num = input().split()
    num_list = []
    for i in num :
        if len(num_list) == 0 :
            num_list.append(i)
            continue
        if num_list[-1] == i :
            num_list.pop()
        else:
            num_list.append(i)

    result = "".join(num_list)

    print(f"#{tc} {result}")