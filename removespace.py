# remove front_space


# sentence = '              today is my first day at the new job.'
# space =' '
# front_space= True
# for letter in sentence:
#     if letter == space and front_space == True:
#         continue
#     else:
#         front_space = False
#         print(letter,end='')

# remove back_space

sentence = '"today is my first day at the new job.              "'
i = len(sentence) - 1
end = 0
while i >= 0:
    if sentence[i] == '':
        i-=1
        continue
    else:
        end = i
        break
    i-=1
i = 0
while i <= end:
    print(sentence[i],end ='')
    i+=1
