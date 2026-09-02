# for row in range(1,6):
#     for col in range(1, row):
#         print("*", end = ' ')
#     for star in range(1,6):
#         print(1, end = ' ')
#     print()

# program :2

# for row in range(1,6):
#     for col in range(1,row+1):
#         print("*", end =' ')
#     for star in range(col+1):
#         print(6-col, end = ' ')
#     print()

for row in range(1,6):
    for col in range(1,6-row):
        print("", end = ' ')
    for col in range(1,row+1):    
        print(6-col,end = ' ')    
    print()