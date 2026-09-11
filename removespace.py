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
space =' '
back_space= True
for letter in sentence:
    if letter == space and back_space == True:
        continue
    else:
        back_space = False
        print(letter,end='')