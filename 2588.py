a=input()
b=input()



b_1= b%10
b_10 = (b%100- b%10)/10
b_100 = b/100

solve_3 = a * b_1
solve_4 = a * b_10
solve_5 = a * b_100
solve_6 = a*b

print(solve_3)
print(solve_4)
print(solve_5)
print(solve_6)

#print(b_100,b_10,b_1)
#print(type(a),b)
