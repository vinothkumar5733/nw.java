sentence = "this is vinoth"
l = sentence.split()
i = len(l) - 1
sentence2 = ""
while i >= 0:
    sentence2 = sentence2 + l[i] + " "
    i-=1
print(sentence2)


# ex2: camel case

name = "vinoth kumar tuticorin"
i = 0
while i < len(name):
    if name[i] == " ":
        print(name[i+1].upper(),end ="")
        i+=1
    else:
        print(name[i],end ="")
        i+=1
        