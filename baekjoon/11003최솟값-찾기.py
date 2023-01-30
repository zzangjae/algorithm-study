import sys
from collections import deque
input = sys.stdin.readline

N, L = map(int, input().split())
num_list = list(map(int, input().split()))

local_deque = deque()

for index in range(N):
    while local_deque and local_deque[-1][1] > num_list[index]:
        local_deque.pop()
    
    if local_deque and local_deque[0][0] < index + 1 - L:
        local_deque.popleft()
    
    local_deque.append([index, num_list[index]])
    print(local_deque[0][1], end = " ")

    


    
