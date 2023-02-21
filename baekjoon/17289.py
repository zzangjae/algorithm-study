n = int(input())
num_lst = list(map(int, input().split()))
stack = []
result = [-1, ]

for idx in range(n-1, 0, -1):

    if num_lst[idx - 1] >= num_lst[idx]:
        while stack:
            top = stack.pop()
            if top > num_lst[idx - 1]:
                result.append(top)
                stack.append(top)
                break
        else:
            result.append(-1)

    else:
        stack.append(num_lst[idx])
        result.append(num_lst[idx])

print(' '.join(map(str, result[::-1])))




