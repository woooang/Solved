
import sys

from pyparsing import empty
N = int(sys.stdin.readline())

stack = []
for i in range(N):
    
    M = sys.stdin.readline().split()

    if M[0]=="push":
        stack.append(M[1])
    elif M[0] == "pop":
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif M[0] == "size":
        print(len(stack))
    elif M[0] == "empty":
        if len(stack)==0:
            print(1)
        else:
            print(0)
    else:
        if len(stack)>=1:
            print(stack[-1])
        else:
            print(-1)

    