testcase = int(input())

for i in range (testcase):
    student = list(map(int,input().split()))
    cnt = 0
    num = student[0]
    score = student[1:]
    avg = sum(score)/num
    
    for j in score:
        if (j>avg):
            cnt+=1

    ratio = cnt/num*100
    print( f'{ratio:.3f}%')
