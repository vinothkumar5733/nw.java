i = 0 
j = 1
while i < len(l):
    if l[i] == 0:
        l[i], l[-j] = l[-j],l[i]
        if j < len(l)//2:
            j+=1
    i+=1
else:
    print(l)