import sys

stack_list = []

def main():
    #while loop counting num.
    n = int(input())
    stack_pointer = -1

    while n>0:
        #input = sys.stdin.readline()
        command = list(map(str,sys.stdin.readline().split()))
       # print(command)
        if 'push' in command:
            stack_list.append(command[1])
            stack_pointer = stack_pointer + 1
        elif 'pop' in command:
            if stack_pointer is -1:
                print('-1')
            else:
                print(stack_list[stack_pointer])
                del stack_list[stack_pointer]
                stack_pointer = stack_pointer-1
            
        elif 'size' in command:
            print(stack_pointer+1)
        elif 'empty' in command:
            if stack_pointer is -1:
                print(1)
            else:
                print(0)
            
        elif 'top' in command:
            if stack_pointer is -1:
                print(-1)
            else:
                print(stack_list[stack_pointer])
        
        
        
        
        n= n-1

main()
#print(stack_list)
