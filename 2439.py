a = int(input())

#x = i+1
for i in range(a):
    for j in range(a-1-i):
        print(" ", end='')
    for k in range(i+1):
        print("*", end='')

    print('')
    #print(i)


#i는 0부터 시작하게 됨.
