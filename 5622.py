alp_list = ['ABC','DEF','GHI','JKL','MNO', 'PQRS','TUV',' WXYZ']
text=input().upper()
time = 0
for i in range(len(text)):
    for k in alp_list:
        if text[i] in k:
            time += alp_list.index(k) + 3
print(time)