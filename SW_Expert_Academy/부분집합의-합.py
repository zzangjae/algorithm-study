def make_subset(set_list):
    subset = [[]]

    for member in set_list:
        size = len(subset)
        for index in range(size):
            subset.append(subset[index]+[member])

    return subset

def main():
    test_case = int(input())
    subset = make_subset(list(range(1, 13)))

    for iteration in range(test_case):
        n, k = map(int, input().split())
        result = 0

        for set in subset:
            if len(set) == n and sum(set) == k:
                result += 1

        print(f'#{iteration+1} {result}')

main()