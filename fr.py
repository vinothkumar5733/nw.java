# totalFeet = 60
# up = 0
# down = 0.5
# day =0
# while up < 60:
#     up = up + 2
#     day = day + 1
#     up = up - down
# print(day)
# print(up)
# print(down)

# ex : 02


totalFeet = 60
up = 2
down = 0.5
day = 0
while totalFeet > 0:
    totalFeet = totalFeet - up + down
    day = day + 1

print(day)