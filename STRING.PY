s = 'akilan'
word = list(s)

print(word)

key = word[0]
count = 1
i = 1
while i < len(word):
    if key != '*' and key == word[i]:
        word[i] = '*'
        count+=1
    i+=1
print(key, 'is present', count, 'times')
print(word)
