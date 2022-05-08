import random

list = []
N=random.randint(1, 1000000)

print(N)
for i in range(N):
    while N in list:
        N=random.randint(1, 1000000)
    list.append(N)

for k in list:
    print(k, end =' ')
print('\n')
print(min(list), max(list))
