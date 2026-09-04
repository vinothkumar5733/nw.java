# for row in range(1,5):
#     for col in range(1,5):
#         if row==1 or row ==4 or col == 1 or col == 4:
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()

# for row in range(1,5):
#     for col in range(1,5):
#         if row == 1 or row ==4 or col == 1 or col == 4:
#             if(row ==4 and col ==4):
#                 print(" ", end =" ")
#             else:
#                 print("*", end = " ")
#         else:
#             print(" ", end = " ")

#     print()

for row in range(1,8):
    for col in range(1,8):
        if col==1 or col ==7 or (row == col and row<=4) or (row+col==8 and row<=4):
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()
