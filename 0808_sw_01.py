t = int(input())
for tc in range(1,t+1):
    n,m = list(map(int,input().split()))


    # word_list = [list(input().split()) for i in range(m)]
    # 리스트로 받아서 2차원 배열을 만들 것인데 제시되는 알파벳이
    # 띄어쓰기가 되어있지 않으므로 split을 사용할 필요가 x
    word_list = [list(input()) for i in range(n)]







    for r in range(n):
        for c in range(m):
            if n%2 == 0 and word_list[r][c] == word_list[n-r-1][c]:
                print(word_list)



