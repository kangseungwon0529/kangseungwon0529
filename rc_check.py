t = int(input())
for tc in range(1,t+1):
    n,m = map(int,input().split())
    pop_list = [list(map(int,input().split())) for _ in range(n)]

    print(pop_list)
"""
1
3 5
2 1 1 2 2 
2 2 1 2 2 
2 2 1 1 2 
"""