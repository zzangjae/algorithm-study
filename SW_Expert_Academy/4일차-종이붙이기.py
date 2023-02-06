'''
Idea
    처음에 너무 어렵게 생각한 것 같다. 
    종이를 붙일 때 세로 1개를 붙이는 경우, 
    가로 2개를 붙이는 경우, 큰 종이를 붙이는 경우
    위 세가지 경우 빼고는 없다는 것을 생각해내면 쉽게 풀 수 있다.

Solution
    1. 종이를 빈틈이 없는 지 확인한다. 빈틈이 없을 경우 완성
    2. 종이를 붙이는 세가지 경우로 분기한다.
        (1 : 세로 한개, 2 : 가로 두개, 3 : 큰 종이 한개)
    3. 각각의 경우에 대해 위 두가지 경우를 반복한다.
    (위 과정을 재귀를 이용하면 쉽게 구현할 수 있을 것 같다.)

    시간제한 걸림...
    stack을 이용해서 풀어볼까;;
    1. 각 순간에 1, 2, 3을 append 가능 하면 스택에 남은 칸 수를 줄여서 append
    ex ) (1, 6), (2, 5), (3, 5)
    칸 수가 0보다 작아지면 pop 안함, 0이면 결과 1 추가
    2. stack에 자리가 있음 pop 해서 1을 진행
    
    이것도 시간제한;;;;;

    순서 배열로 풀어보자.
    1. stack에 남은 칸 수를 저장
    2. 짝수 -> 2 ^ (n // 2) * (n // 2 + stick)! /  stick
'''

import sys
sys.stdin = open("input.txt", "r")

t = int(input())

# def dfs(base):

#     if 0 not in base:
#         global result 
#         result += 1 if 2 not in base else base.count(2)
#         print(base)
#         return 

#     start_idx = base.index(0)

#     for condition in range(1, 4):
        
#         temp_base = base[:]

#         if condition == 1:
#             temp_base[start_idx] = 1
#             dfs(temp_base)

#         elif condition == 2 and start_idx < n - 1:
#             temp_base[start_idx : start_idx + 2] = [2, 2]
#             dfs(temp_base) 
def factorial(blocks):
    if blocks <= 1:
        return 1
    else:
        return blocks * factorial(blocks - 1)


for iteration in range(t):
    n = int(input()) // 10
    k = 0
    stack = [(k, n)]
    result = 0

    while stack:
        stick, space = stack.pop()

        if space == 0:
            result += 1
            break

        elif space % 2:
            stack.append((stick+1, space-1))

        else:
            result += (2 ** (space//2) * factorial(space//2 + stick) // factorial(stick)) // factorial(space//2)
            stack.append((stick+1, space-1))
        
    print(f'#{iteration+1} {result}')
    