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

# ex : 03
totalfeet = 60
up = 2
night = 0.5
days = 0
while totalfeet > 0:
    days += 1
    totalfeet -= up
print(days)    

# ex : 04

no = 1
while no <=5:
    print(no)    # 1 2 3 4 5 
    if no == 5:
        break

    no+=1
else:
    print(no+10)

# ex : 05
no = 1
while no <=5:
    print(no)    # 1 2 3 4 5 
    no+=1    
else:
    print(no+10) 


# ex : 06

saint = 1
temple = 0
while temple < 5: