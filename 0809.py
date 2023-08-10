t = int(input)
for tc in range(1,1+t):
    n = int(input())
    # 배열을 만들고 그 값을 저장한다.
    n_list = [1] * (n+1)
    print(f"#{tc}")
    for i in range(n):
        if n <2:
            return n
        else:
            return n_list(n-1) + printn_list(n-2)

        print(f"{n_list}")
t = int(input())
for tc in range(1, t + 1):
    # 입력값이 문자형이므로 인풋으로만 받아준다.
    word = input()
    # word가 정리 될 수 있는 공간을 만들어줘야하는데..? []가 아닌 "" 로쓰면 어떻게 될까
    # 테스트 해보니 append자체가 리스트에 쓰이는 ()()함수이므로 ""로는 못받음
    re_word = []
    # i는 word에 있는 문자 그대로로 비교할 것이므로 레인지 설정없이 그냥 받아준다.
    for i in word:
        # reword 에 값이 하나도 없으면 채워줘야 이후 비교가 가능하므로 공간을 확인한다.
        if len(re_word) == 0:
            re_word.append(i)

        # if 를 사용해서 받을때는 위의 내용이 pass 가 되게 만들어주고 아닐때는 elif 로 받아주면 된다.
        elif re_word[-1] != i:
            re_word.append(i)
        else:
            re_word.pop()

    print(f"#{tc} {len(re_word)}")

"""

1
ABCCB
"""