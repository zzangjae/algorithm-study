def find_terminal(k, startindex, bus_terminal, result=0):
    
    n = len(bus_terminal)-1

    for index in range(k+startindex, startindex, -1):
        if index >= n:
            return result

        if bus_terminal[index] == 1:
            return find_terminal(k, index, bus_terminal, result+1)

    return 0


def main():
    test_case = int(input())
    
    for iteration in range(test_case):
        k, n, m = tuple(map(int, input().split()))
        terminal_num = list(map(int, input().split()))
        bus_terminal = [0] * (n+1)

        for index in terminal_num:
            bus_terminal[index] += 1

        print(f'#{iteration+1} {find_terminal(k, 0, bus_terminal)}')

main()



