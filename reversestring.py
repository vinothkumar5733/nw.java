sentence = "this is vinoth"
l = sentence.split()
i = len(l) - 1
sentence2 = ""
while i >= 0:
    sentence2 = sentence2 + l[i] + " "
    i-=1
print(sentence2)