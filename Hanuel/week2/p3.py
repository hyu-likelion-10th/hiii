s = input().upper()
d = {}

for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

max = 0
for key,value in d.items():
    if value > max:
        max = value
        arr = [key]
    elif value == max:
        arr.append(key)
if len(arr) >= 2:
    print("?")
else:
    print(arr[0])