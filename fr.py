totalFeet = 60
up = 2
down = 0.5
day =1
while up < 60:
    up = up + 2
    day = day + 1
    up = up - down
print(up)

