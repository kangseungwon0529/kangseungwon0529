t = 10
for tc in range(1,t+1):
    # 단어의 길이와 단어의 내용이 함께 제시되므로 두개를 나누어 받아준다.
    size,num = input().split()
    size = int(size)
    # 스텍의 크기는 단어의 길이가 제시되어지고 있다.
    stack = [0]*size
    #top = 마지막으로 삽입한 위치인데, 처음엔 아무런 값도 스텍에 없기 때문에 -1부터 시작
    # 0부터 시작해서 더하기를 해주지 않아도 된다.
    top -=1
    #하지만 밑에서 값이 추가가 될때마다 top에 +-1을 해줄 것이기 때문에 0 부터시작
    #top에 문자를 하나 넣는다는 의미로 top에 +1을 해줄것이다.
    # top 에 1을 더해주면서 top의 값은 0 이되었고
    # stack[top] 또한 stack[0]과 같은 값을 가짐. 그 위치에 num의 천번째 자리값을 넣어줄 것이다.
    stack[top] = num[0]
    print(stack[top])
    #이제 스텍의 탑위치와 num의 숫자를 비교하여 넣어줄 것이다. 넘버의 길이많큼 비교
    for i in range(1,len(num)):
        # stack[0]에 이미 num 인덱스 0번 자리값을 넣어줬으므로 값이 있다고 가정하고 넣어준다.
        # 하지만 반복이 되기 때문에..? 이미 앞에서 다 빠지게 되었을 경우를 고려하며 0이 아닌 경우를 작성해 주어야한다.
        if stack[top] != num[i] :
            stack.append(num[i])
            top += 1

        else:
            stack.pop()
            top -= 1
    print(stack)


















"""
word = 1238099084


10 1238099084
"""