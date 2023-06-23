"""
제목: AC

조건:
1. 1초, 256MB
2. R -> 배열에 있는 수의 순서 뒤집기
3. D -> 첫 번쨰 수를 버리는 함수
4. 배열이 비어있는데 D를 사용한 경우 에러를 나타나게 해야됨
5. 1 <= T <= 100, 1 <= p <= 100,000, 0 <= n <= 100,000

idea:
1. 각 기능을 정확히 구현해야됨 + 출력 값도 준수해야됨
2. O(n)으로 작동해야됨 -> 실제 배열을 계속 순서를 뒤집고 삭제하는 것이 아닌
    가상으로 뒤집고 이를 index에 start와 end 변수를 이용해서 추적하자.

solution:
1. T 입력받기
2. for 문 이용하여 함수, 배열 입력받기
3. 입력 받은 함수를 이용하여 is_reversed, start, end 변수값 구하기
4. 구한 정수 값 이용하여 적절한 값 출력하기
"""

# 1. T 입력받기
t = int(input())
# 2. for 문 이용하여 함수, 배열 입력받기
for _ in range(t):

    function_lst = list(input())
    num_count = int(input())
    num_lst = input()[1:-1].split(',') if num_count else input()

    # 3. 입력 받은 함수를 이용하여 is_reversed, start, end 변수값 구하기
    is_reversed = False
    start = 0
    end = num_count

    for func in function_lst:

        if func == 'R':
            is_reversed = not is_reversed

        if func == 'D':

            if is_reversed:
                end -= 1

            else:
                start += 1

    # 4. 구한 정수 값 이용하여 적절한 값 출력하기
    if end - start < 0:
        print('error')

    else:
        if is_reversed:
            print('[' + ','.join(num_lst[start:end][::-1]) + ']')

        else:
            print('[' + ','.join(num_lst[start:end]) + ']')


