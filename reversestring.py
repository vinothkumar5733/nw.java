sentence = "this is vinoth"
l = sentence.split()
i = len(l) - 1
sentence2 = ""
while i >= 0:
    sentence2 = sentence2 + l[i] + " "
    i-=1
print(sentence2)


# ex2: camel case

# name = "vinoth kumar tuticorin"
# i = 0
# while i < len(name):
#     if name[i] == " ":
#         print(name[i+1].upper(),end ="")
#         i+=1
#     else:
#         print(name[i],end ="")
#         i+=1


# word1 = input("Enter word: ") #cat 
# word2 = input("Enter word: ") #act 

# if len(word1) != len(word2):
#     print("Not anagram")
# else:
#     for letter in word1: #cat
#         if word1.count(letter) != word2.count(letter):
#             print('Not anagram')
#             break 
#     else:
#         print('Anagram')
        