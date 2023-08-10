#처음에 나타내는 반복되는 횟수를 받아줄 요소
t = int(input())
# 반복되는 횟수가 정해질 범위
for _ in range(t):
# 출력될 테스트 케이스를 받아줄 인자 #num = 정수형으로 표현할 수 없으므로 이어지는 두 입력값을 나누어서 받기만 먼저한다.
    tc, lenth = input().split()
    #길이를 나타내는 lenth는 숫자로 표현되어야 하므로 int를 씌워 변환해준다.
    lenth = int(lenth)
    #이어지는 문자열읃을 받아와야 하므로 입력값들을 문자열로 변환하고 리스트를 씌워준다.
    tc_list = list(map(str,input().split()))
    # 각 인자들의 숫자를 세어줄 카운팅을 위한 딕셔너리 구성
    num_dict = {"ZRO": 0, "ONE": 0, "TWO": 0, "THR": 0, "FOR": 0, "FIV": 0, "SIX": 0, "SVN": 0, "EGT": 0, "NIN": 0}
    #tc_list 의 인자값
    for num in tc_list:
        num_dict += 1
    # 정렬한 것이 들어갈 수 있는 리스트값
    sort_num = []
    # 순차정렬로 정렬해준다.
    for i in range(len(tc_list)-1,-1,-1):
        sort_num[num_dict[tc_list]] = num_dict[tc_list]
        sort_num.append(sort_num[num_dict[tc_list]])

    print(f"{tc} {sort_num}")