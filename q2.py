n = int(input())
lgr = {}
for i in range(n):
    t = input().split()
    if t[0].upper() == "ADD":
        lgr[t[1]] = lgr.get(t[1], 0) + int(t[2])
    if t[0].upper() == "REMOVE":
        print(f'{lgr.pop(t[1], "Not Found")}')
win = -1001000
winner = 0
for t, x in lgr.items():
    if x > win:
        winner = t
        win = x 
    print(f'{t} {x}')
print(f'Winner: {winner}' if winner else "No Teams")