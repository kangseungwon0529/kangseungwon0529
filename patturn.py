t = "This is a book~!" # 전체 문자
p = "is" # 찾을 문자
n  = len(t) #전체 문자의 길이 큰거
m = len(p) # 찾을 문자의 길이 작은거

i = 0 # t의 인덱스 값 = ti = 전체 문자의 인덱스 값
j = 0 # p의 인덱스 값 = pi = 작은 문자의 인덱스 값


while i<n and j < m: #전체 문자, 찾을 문자의 인덱스 값이 전제 문자, 찾을 문자의 길이 보다 작을 때


    if p[j]  == t[i] :
        j += 1
        i += 1

    elif t[i] != p[j]:
        i = i-j
        j = -1

if j==m : # return i - m