n = int(input())
re = {}
for i in range(n):
    s1 = input().split()
    re[s1[0]] = s1[1]
m = int(input())
t = ""
for j in range(m):
    s2 = input()
    t = t + re.get(s2, "Not Enrolled") 
    
    if j < (m-1): t = t + "\n"
print(t)