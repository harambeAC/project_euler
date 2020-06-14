prev = 1
cur = 2

s = 0

while cur < 4000000:
    if(cur%2 == 0):
        s += cur
        print(cur)

    tmp = cur
    cur += prev
    prev = tmp

print(s)