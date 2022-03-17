n = int(input())
m = int(input())

cnt = 0
list = [1]

while cnt!=1:
    cnt = 0
    cnt = (list[-1] + (m-1)) % n
    if cnt != 0:
        list.append(cnt)
    else:
        list.append(n)
list.pop()

print(''.join(map(str, list)))