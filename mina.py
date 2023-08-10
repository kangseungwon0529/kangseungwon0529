t = int(input())
for tc in range(1,t+1):

    word = input()
    word_list = []

    for i in word:
        if len(word_list) == 0:
            word_list.append(i)
        if word_list[-1] != i:
            word_list.append(i)
            break
        elif word_list[-1] == i:
            word_list.pop(i)


    print(f"#{tc} {len(word_list)}")