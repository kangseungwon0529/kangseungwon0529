text = input()
size = 1000
stack = [0] * size
top = 0
#스텍을 이용해서 풀건데
#일단 문자를 스텍에 넣어(맨처음 글자는 넣음
top +=1
stack[top] = text[0]
#두번째 글자부터는 내가 제일 최근에 넣었던 글자와 비교해서
#만약 같다면 스택에서 pop
#다르다면 현재글자를 스텍에
    for i in range(1,len(text)):
        if top != -1 and stack[top] == text[i]:
            top -=1
        #다르다면 현재 글자를 스택에 push
        else:
            top += 1
            stack