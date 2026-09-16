word = 'abcd'
i = 1
while i < len(word):
    print(word[i],end="")
    i+=1
print(word[0])

#  ex:2

word = 'abcd'
print(word[-1]+word[:-1])