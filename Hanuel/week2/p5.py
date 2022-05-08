def solution(phone_book):
    answer = True
    phone_book.sort()
    size = len(phone_book)
    for i in range(0,size-1):
        checksize = len(phone_book[i])
        if phone_book[i+1][:checksize] == phone_book[i]:
            answer = False
            break
    return answer