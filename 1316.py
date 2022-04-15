count = 0
for i in range(int(input())):
    text = input()
    non_group = 0
    for k in range (len(text)-1):
        if text[k] != text[k+1]:
            new_text = text[k+1:]
            if new_text.count(text[k]) >0:
                non_group +=1
    if non_group == 0:
        count +=1
print(count)