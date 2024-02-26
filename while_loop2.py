#while loop only printing the even values
start = int(input())

end = int(input())

while start <= end:
    if start % 2 == 0:
        print(start)
    start += 1
     