t = int(input())
for tc in range(1,t+1):
    word = input()
    word_list = []

    for i in word:
        if len(word_list) == 0 :
            word_list.append(i)
            print(word_list)
        if word_list[-1] == i :
            word_list.pop(i)
            return
