n = int(input())
grade = list(map(int, input().split()))
grade = grade[:n]
highgrade = max(grade)
average = []
for i in range(len(grade)):
    average.append((grade[i]/highgrade)*100)
average = sum(average)/n
print(average)