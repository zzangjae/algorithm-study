t = int(input())

for idx in range(t):
    x, y = input(), input()
    if x in y:
        print(f'#{idx+1} 1')
    else:
        print(f'#{idx+1} 0')

