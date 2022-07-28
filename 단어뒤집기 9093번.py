from audioop import reverse


N = int(input())

for i in range(N):
    temp = list(input().split(" "))
    for k in temp:
        print(k[::-1],end=" ")

