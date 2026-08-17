# p=7
# d=2
# if d%p == 0:
#     print('not a prime')
#     d+=1
# else:
#     print(d)
#     print('prime')


# # # ex:02

# n = 1319
# d=2
# while d<n:
#     if n%d ==0:
#         print('not a prime')
#         break
#     d+=1
# else:
#     print(n)
#     print('prime')

# # ex:03

# n = 1319
# d = 2
# while d <= n//2:
#     if n%d == 0:
#         print('not a prime')
#     d+=1
# else:
#     print(d)
#     print('prime')


# # ex:04

# num = 1024
# div = 3
# while div<=2:
#     if num *div !=0:
#         print('prime')


# # ex:05
# i = 4
# n = 1
# while n!=i:
#     if n*1 and n**1:
#         print('not valid')
        


# ex:06

# security =12
# divider = 2
# while divider <= security:
#     if security % divider == 0:
#         if security % divider == 0 !=2:
#             print("number")
#         print("not prime")
#         break
#     diviser+=1
# else:
#      print("prime")

# ex:06:

# def find_vip(no):
#     div = 2
#     while div <= no//2:
#         if no % div == 0:
#             return 'not vip'
#         div+=1
#     else:
#         return 'vip'

# no =2
# count = 0
# while count < 5:
#     result = find_vip(no)
#     if result == 'vip':
#         print(no)
#         count+=1
#     no +=1


# ex:08

balance = 8
eaten =0
while eaten < 3:
    eate =balance//2
    balance+=eate
    eaten+=1
print("total",balance)

# balance = 8
# count = 0
# while count < 3:
#     eaten = balance // 2
#     balance+= eaten
#     count+= 1

# print("total", balance)