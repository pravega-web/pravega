l = {}
for t in range(int(input())):
    code = input()
    value = [0,0,0,0,0,0,0,0,0,0]
    for digit in range(10):
        if str(digit) in code:
            value[digit]=1
    if tuple(value) in list(l.keys()):
        l[tuple(value)]+=1
    else:
        l[tuple(value)] = 1

keys = list(l.keys())
keys.sort()
count=0
for a in keys:
    for b in keys:
        if [a[digit] or b[digit] for digit in range(10)] == [1,1,1,1,1,1,1,1,1,1]:
            if a==b:
                count+= l[a]*(l[a]-1)/2
            else:
                count+=l[a]*l[b]/2
print(int(count))
