#  print all even numbers from 1 to N
N = int(input())
i = 1
while i <= N:
    if i % 2 == 0:
        print(i, end=" ")
    i = i+1