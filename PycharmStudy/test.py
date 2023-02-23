import sys
sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())

temp_k = []
temp_v = []

for _ in range(N):
    L, H = map(int, sys.stdin.readline().split())
    temp_k.append(L)
    temp_v.append(H)

garage = sorted(dict(zip(temp_k, temp_v)).items())

if garage[0][1] > garage[-1][1]:
    garage = garage[::-1]

for t in range(len(garage)):
    garage[t] = list(garage[t])

top = [0, 0]
for i in range(len(garage)):
    if top[1] < garage[i][1]:
        top = garage[i]

count = 0
while True:
    if garage[0][1] == top[1]:
        garage = garage[::-1]
        if garage[0][1] == garage[-1][1]:
            count += (abs(garage[0][0] - garage[-1][0]) + 1) * garage[0][1]
            break
    count += (abs(garage[0][0] - garage[-1][0]) + 1) * garage[0][1]
    minus = garage.pop(0)[1]
    for j in range(len(garage)):
        garage[j][1] -= minus

    while True:
        for k in range(len(garage)):
            if garage[k][1] <= 0:
                garage.pop(k)
                break
        else:
            break

print(count)