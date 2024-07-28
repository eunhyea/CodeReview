# < 최대공약수 gcd >

# math 모듈
import math
gcd(x, y)

# 유클리드 호제법
def gcd(x, y):
   # y가 0이 될 때까지 반복
   while y:
       # y를 x에 대입
       # x를 y로 나눈 나머지를 y에 대입
       x, y = y, x % y
   return x


# < 여러 수의 최소공배수 >

# math 모듈
import math
def lcm(x, y):
    return x * y // math.gcd(x, y) # 두 수의 최소공배수
def lcms(array):
  n = arr[0]
  for i in arr[1:]:
    n = lcm(n,i) # 모든 원소들을 차례대로 반복하여 최소공배수를 구함
  return n

# while문 사용
a,b,c = map(int, input().split())
d = 1
while d%a!=0 or d%b!=0 or d%c!=0 :
    d += 1
print(d)
