y = [0, 300, 380, 340, 230, 240, 320, 375, 345, 110, 0]
ans = 0
for i in range(len(y)-1):
    ans += 50*(y[i] + y[i+1])

print(ans)
