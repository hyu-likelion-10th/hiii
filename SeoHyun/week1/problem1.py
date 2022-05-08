num = list(input().split())
num1 = int(''.join(reversed(num[0])))
num2 = int(''.join(reversed(num[1])))

if(num1>num2):
    print(num1)
else:
    print(num2)
