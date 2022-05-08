import random

A=random.randint(100,999)
B=random.randint(100,999)
print(A, B)

reverse_A=int(str(A)[::-1])
reverse_B=int(str(B)[::-1])

if reverse_A > reverse_B:
    print(reverse_A)
else:
    print(reverse_B)
