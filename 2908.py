num = list(map(str,input()))
num.reverse()
num1 = int(''.join(num[:3]))
num2 = int(''.join(num[4:]))
if num1 > num2:
    print(num1)
else:
    print(num2)
