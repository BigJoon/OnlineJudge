a, b = input().split()
n = int(a)
x = int(b)
#n과 x를 입력받고 타입클래스를 int형으로 바꿔줌

c = list(map(int,input().split()))

for i in range(n):
    if c[i] < x:
        print(c[i],end=' ')


#print('len : ',len(c))
#print(c)


#print(a,b)
