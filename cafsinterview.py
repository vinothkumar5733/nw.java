string = "malayalam"
result = ""
for letter in string:
    if letter not in result:
        result+=letter
print(result)
