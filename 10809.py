from string import ascii_lowercase
s = list(map(str, input()))
alpa = list(ascii_lowercase)
position = [-1 for i in range(26)]
for i in range(len(s)):
    for k in range(len(alpa)):
        if s[i] == alpa[k]:
            position[k] = s.index(s[i])
for j in range(len(position)):
    print(position[j], end=' ')
