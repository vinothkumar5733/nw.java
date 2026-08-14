p=7
d=2
if d%p == 0:
    print('not a prime')
    d+=1
else:
    print(d)
    print('prime')


# ex:02

n = 1319
d=2
while d<n:
    if n%d ==0:
        print('not a prime')
        break
    d+=1
else:
    print(n)
    print('prime')