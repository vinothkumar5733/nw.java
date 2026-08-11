guard = 0
lashes = 1024
while lashes > 1:
    lashes //=2
    guard +=1
    print(lashes)
    print(guard)
print('guard count is:', guard)

# ex : 02

police = 0
thief = 40
while thief > police:
    police = police + 2
    print('police:', police)
    print('thief:', thief)


# ex : 03

police, thief = 0, 40
step = 0
while thief > police:
    police = police + 5
    thief = thief + 2
    step+=1
print(police)
print(step)
