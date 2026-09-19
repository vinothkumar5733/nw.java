# EX:01
word = 'abcd'
i = 1
while i < len(word):
    print(word[i],end="")
    i+=1
print(word[0])

#  ex:2

# word = 'abcd'
# print(word[-1]+word[:-1])

# # EX:02

# s = 'VINOTH KUMAR'
# word = list(s)

# print(word)

# index = 0
while index < len(word):
    key = word[index]
    count = 1
    i = index + 1
    while i < len(word):
        if key != '*' and key == word[i]:
            word[i] = '*'
            count+=1
        i+=1
    if key != '*' and count==1:
        print(key, 'is present', count, 'times')
    index+=1
print(word)