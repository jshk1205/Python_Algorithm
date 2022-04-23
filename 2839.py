n= int(input())
total = 0
while n >= 0:
    if n%5 == 0:
        total += n//5
        print(total)
        break
    n -= 3
    total +=1
else:
    print('-1')
