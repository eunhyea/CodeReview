# 6083 가능한 모든 조합 구하기 by itertools

# 방법1) 중첩 for문
x,y,z = map(int, input().split())

for i in range(0,x):
    for j in range(0,y):
        for k in range(0,z):
            print(i,j,k)
print(x*y*z)

# 방법2) itertools.product
import itertools

x,y,z = map(int, input().split())

    # 리스트 정의
a = [i for i in range(0, x)]
b = [i for i in range(0, y)]
c = [i for i in range(0, z)]

    # 가능한 모든 조합 생성 및 출력
for combination in itertools.product(a, b, c):
    print(combination)

    # 가능한 조합의 개수
print(x*y*z)


# 6091 최소공배수 구하는 방법
a,b,c = map(int, input().split())
d = 1
while d%a!=0 or d%b!=0 or d%c!=0 :
    d += 1
print(d)


# 6098 개미 미로
box = [list(map(int, input().split())) for i in range(10)]

while (x<9) and (y<9) :
    
    if box[x][y] == 2:
        box[x][y] = 9
        break
    
    box[x][y] = 9

    if box[x][y + 1] != 1:
        y += 1  # 조건에 맞으면 오른쪽으로 이동
    
    elif box[x + 1][y] != 1:
        x += 1  # 아래로 이동
    
    else : break # 더 이상 이동할 수 없으면 종료

# 결과 출력
for row in box:
    print(" ".join(map(str, row)))
