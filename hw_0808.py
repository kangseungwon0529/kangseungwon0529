t = 10 # 문제에서 제시되는 tc의 개수가 10개라고 알려줌
for tc in range(1,t+1): # 제시되는 만큼의 테스트 케이스를 반복하기 위한 반복문
    check_point = int(input())
    # 8*8 배열을 만들고 그 안에 값을 넣기 위한 2차원 배열을 만들기 위한 변수 제작
    # 배열 안에 들어가는 인자들이 문자형 자료이므로 input.split으로 나누어 받아주고
    # 리스트를 씌워준다.
    n = 8 # 8*8 배열을 만들고 이후에도 쓰기 편한 변수 지정
    board_list = [list(input().split()) for i in range(n)]
    cnt = 0 # 만들어진 회문의 갯수를 파악하기 위한 총량의 값
    # 행 우선 탐색으로 볼 것이므로 행의값과 회문을 지정하는 길이 값을 기반으로 탐색해보자
    for r in range(n) : # 행의 값의 범위를 지정한다.
        # 정방형 사각형이므로 범위는 n으로 동일하게 하지만 직선 네모가 움직일 수 있는 구간을 구해줘야하므로 구간합개념 적용

        for c in range(n - check_point +1):
            # 문자형인 인자 값이 들어오기 위한 변수를 만들어주어야 하므로 변수 = ""로 표현
            check_val = ""
            for k in range(check_point): # 구간을 이동하는 상자의 크기!
                check_val += board_list[r][c+k]
            print(check_val)

            # 이제 상자가 만들어졌으니 상자 안의 자료가 회문구조인지를 파악해주는 공식을 적어줘야함
            # for lif check_point
