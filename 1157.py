text =input().upper()
text_set = list(set(text))
cnts_list = []
for i in text_set:
    cnt = text.count(i)
    cnts_list.append(cnt)
if cnts_list.count(max(cnts_list)) > 1:
    print('?')
else:
    print(text_set[cnts_list.index(max(cnts_list))])