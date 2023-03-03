import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
num_lst = list(map(int, input().split()))
operator_lst = list(map(int, input().split()))
minimum = 1000000000
maximum = -1000000000


def dfs(depth=0, result=0):

    if depth == n-1:
        global minimum, maximum

        if result < minimum:
            minimum = result

        if result > maximum:
            maximum = result

        return

    for idx in range(4):
        if operator_lst[idx] != 0:

            if idx == 0:
                operator_lst[idx] -= 1
                dfs(depth + 1, result + num_lst[depth+1])
                operator_lst[idx] += 1

            elif idx == 1:
                operator_lst[idx] -= 1
                dfs(depth + 1, result - num_lst[depth+1])
                operator_lst[idx] += 1

            elif idx == 2:
                operator_lst[idx] -= 1
                dfs(depth + 1, result * num_lst[depth+1])
                operator_lst[idx] += 1

            elif idx == 3:
                operator_lst[idx] -= 1
                dfs(depth + 1, int(result / num_lst[depth+1]))
                operator_lst[idx] += 1


dfs(0, num_lst[0])
print(maximum)
print(minimum)




