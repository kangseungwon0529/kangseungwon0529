t= int(input())

for tc in range(1,t+1):
    n,m = map(int,input().split())
    #n의 값은 글자판의 가로세로 크기, m은 길이가 m 인 회문을 지시
    #글자모움 (2차원배열로 만들기)
    text = [list(input()) for _ in range(n)]
    
    # 우리가 찾는 회문 = 정답을 도출하기 위헤 미리 적어놓은 매개변수
    answer = ""
    # indented error = for 문 안에 들어갈 값이 있어야하는데 그것을
    # 뒷받침해주는것이 없을때 뜨는 에러
    # 행 우선순회
    # rc로 이루어진 이차원배열에서 선을 그어 나타내는 것이므로 그 선이 움직일 수 있는
    # 행 또는 열에 선의 이동범위를 제한해 줄 수 있는 구간합 적용
    for i in range(n): #i 는 행번호
        for j in range(n - m + 1): #j 는 열번호
            #(i,j)위치에 있는 글자부터 회문을 만들기시작
            #회문의 길이가 m이니까 (i,j)~(i,j+m)까지의 글자를 모아서
            # 문자열로 만들면 완성 => 이 문자열이 회문인지 아닌지 검사
            # j 의 범위 조심! (인덱스 벗어나지 않도록

            word_row = ""
            #글자를 m개 모아서 문자열 만들기
            # print(m)
            for k in range(m):
                word_row += text[i][j+k]
            # print(word_row)

    # word_row가 회문인지 아닌지 판별(인덱스 연산)
    # word_ row 가 회문이다 ==> answer = word_row
            for l in range(len(word_row)//2):
                if word_row[l] != word_row[-1-l]:
                    break
            else: # 반복문 안에서 break문을 만나지 않으면 실행
                answer = word_row
                # print(answer)

    #열 우선순회
    for j in range(n): # text상자가 움직일 수 있는 j 열 번호
        for i in range(n-m+1): # i는 행 번호

            word_col = ""

            for l in range(m):
                word_col += text[i+l][j]

            for c in range(len(word_col) // 2):
                if word_col[c] != word_col[-1 - c]:
                    break
            else:
                answer = word_col
    #
    print(f"#{tc} {answer}")


"""

1
10 10
GOFFAKWFSM
OYECRSLDLQ
UJAJQVSYYC
JAEZNNZEAJ
WJAKCGSGCF
QKUDGATDQL
OKGPFPYRKQ
TDCXBMQTIO
UNADRPNETZ
ZATWDEKDQF
"""