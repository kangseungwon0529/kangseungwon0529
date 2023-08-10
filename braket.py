t = int(input())

for tc in range(1, t + 1):
    row = input()  # 짝이 맞는지 알아보기 위한 문자열들을 입력

    stack = []  # 스택을 구현하는것

    answer = 1
    print(row)
    print()
    # 괄호검사
    for i in row:
        # row에서 한글자씩 떼어와서 검사
        if i == "(" or "{":
            stack.append(i)
            print(stack)
            print()
        if i == ")" or "}":
            if len(stack) == 0:
                answer = 0
                break
            b = stack.pop
            if not(b == "(" and i == ")"):
                answer = 0
                pass
            if not(b == "{" and )

    if len(stack) > 0 :
        answer = 0
    print(stack)

    # 떼어낸 한글자가 여는 괄호면? 스택에 삽입
    # 떼어낸 글자가 닫는 괄호다 => 스텍에서 하나 꺼내온다음에
    # 짝이 맞는지 검사
    # 꺼내오기전에 스택이 비어있나 확인, 비어있으면 오류

    # 모든 검사후 스택이 비어있지 않으면 오류
    print(f"{tc} {answer}")

"""
1
print('{} {}'.format(1, 2))
N, M = map(int, input().split()) 
print('#{} {}'.format(tc, find())

"""

