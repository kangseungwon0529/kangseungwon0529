t = int(input())

for tc in range(1,t+1):
    word = list(input())
    num = len(word)

    for i in range(len(word)):
        for i in range(1,num):

            if word[i-2:i-1] == word[i-1:i]:
                word.pop(i-1), word.pop(i-2)
                num -= 1

    print(f"#{tc} {len(word)}")







    """
1
ABCCB
    """