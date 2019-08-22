a,b= input().split()

hour = int(a)
minute =int(b)


if minute>=45:
    print(hour,minute-45)
else:
    if hour is 0:
        print(23,minute+60-45)
    else:
        print(hour-1,minute+60-45)
#print(hour,minute)
#print(type(hour),type(minute))

