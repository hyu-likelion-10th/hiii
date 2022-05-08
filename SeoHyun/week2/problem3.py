word = input().upper()
dic = {}
cnt = 1

for i in word:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] = dic[i]+1
        
max_key = max(dic,key=dic.get)

def findkey(dict, val):
  return list(key for key, value in dict.items() if value == val)

m = findkey(dic, dic[max_key])

if((len(m)>1)&(len(word)!=1)):
    print("?")
else:
    print(max_key)
