# l1=[10,20,30]
# l2=[40,50,60]
# l=[l1,l2]
# print(l[0][0])
# print(l[1][1])

# LIST DAY 02

# l1 = [10,20,30]
# l2 = [40,50,60]
# l3 = [70,80,90]

# l = [l1,l2,l3]
# result = sum(l1)+sum(l2)+sum(l3)
# average = result/3
# print(result)
# print(average)

# LIST DAY 03

# l1 = [10,20,10,20,30,40]
# l2 =list(set(l1))
# print(l2)

# ex:02
l3 = [10,20,10,20,30,40]
l4 =[]
for i in l3:
    if i not in l4:
        l4.append(i)
print(l4)