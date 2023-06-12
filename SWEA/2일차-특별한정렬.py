def alternately_sort(arr):
    arr.sort()
    n = len(arr)
    i = 0
    j = n - 1
    result = [None] * n
    for k in range(n):
        if k % 2 == 0:
            result[k] = arr[j]
            j -= 1
        else:
            result[k] = arr[i]
            i += 1
    return result

test_case = int(input())

for case in range(test_case):
    n = int(input())
    number_lst = list(map(int, input().split()))
    number_lst = list(map(str, alternately_sort(number_lst)))
    print(f'#{case+1} '+ ' '.join(number_lst[:10]))