student = [80,75,90,60,85]

for i in range(1,4):
    print(student[i],end=' ')
  
def sum(a,b):
    y = a+b
    return y
start = 0
for i in student:
    start = sum(start,i)
l = len(student)
print(start/l)
print(student)
student.append(95)
print(student)
student.sort(reverse=True)
student.pop()
student.sort()
print(student)





