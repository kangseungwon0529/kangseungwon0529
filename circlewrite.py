t = int(input()) #받아야하는 tc가 3회임
for tc in range(1,t+1):
    word = list(input())
    result = 0
    # print(word)
    for i in range(len(word)//2) :
        # print(word[i] , word[-1-i], -1-i)
        if word[i] == word[-1-i]:
            result = 1
        else:
            result =  0


    print(f"#{tc} {result}")


"""
opaaiu
"""
