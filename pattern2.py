# for row in range(1,6):
#     print(row)
#     for col in range(1,row+1):
#         print((6-col)*row, end = ' ')
#     print()

for num in range(6,1,-1):
    for col in range(1,num): #1 2 3 4 5
        print(num-col, end=' ')
    print()
