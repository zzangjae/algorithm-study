import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for iteration in range(t):
    n, m = map(int, input().split())
    pizza_lst = list(map(int, input().split()))
    pizza_lst = [[i, pizza_lst[i]] for i in range(m)]
    queue = pizza_lst[:n]
    pizza_lst = pizza_lst[n:]
    front = 0
    last_pizza_idx = 0

    while queue:

        if queue[front][1] == 0:
            last_pizza_idx = queue[front][0]
            if len(pizza_lst) > 0:
                queue[front] = pizza_lst.pop(0)
            else:
                del queue[front]
                n -= 1

                if n == 0:
                    break

                front = front % n
                continue

            front = (front + 1) % n

        else:
            queue[front][1] = queue[front][1] // 2
            if queue[front][1] == 0:
                continue

            front = (front + 1) % n

    print(f'#{iteration + 1} {last_pizza_idx + 1}')

