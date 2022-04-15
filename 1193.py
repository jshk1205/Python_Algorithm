line = 1
x = int(input())
while x > line:
    x -= line
    line += 1
if line %2 ==0:
    mol = x
    den = line - x + 1
else:
    mol = line - x + 1
    den = x
print(mol, '/', den , sep='')
#시간 초과되는 코드
# mol, den = 1, 1
# for i in range(1, int(input())):
#     if (mol+den) % 2 == 0:
#         if mol > 1:
#             mol -= 1
#         den += 1
#     else :
#         if den > 1:
#             den -= 1
#         mol += 1
# print(mol,'/',den, sep='')
