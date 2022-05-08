def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    size = len(participant)
    for i in range(0,size):
        if i==size-1:
            answer = participant[-1]    
        elif participant[i] != completion[i]:
            answer = participant[i]
            break
    return answer
