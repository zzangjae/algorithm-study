"""
이름: 색종이 만들기

조건:
1. 1초, 128MB

idea:
1. 한변의 길이가 최대 128이므로 재귀를 이용하면 최악의 경우라 하더라도 128 * 128 * a 번 실행되므로 1초 안에 실행 가능하다.
    꼼꼼하게 구현하는 것이 관건이 될 것 같다.

solution:
1. 종이의 한 변의 길이 n을 입력받고, 종이의 색칠 현황을 이차 배열 형태로 입력 받는다.
2. 잘라진 흰색 종이와 파란색 종이의 개수를 pair 형태로 반환하는 함수를 작성한다.
    - 변의 길이가 1이면 (1, 0) 또는 (0, 1) 반환
    - 주어진 index 범위의 종이 색깔을 확인하여 모두 같은 색깔이면 pair 반환
    - 모두 같은 색깔이 아닐 경우 index를 분할하여 4번의 재귀 실행
3. 결과 값 출력
"""

# 1. 종이의 한 변의 길이 n을 입력받고, 종이의 색칠 현황을 이차 배열 형태로 입력 받는다.
n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]


# 2. 잘라진 흰색 종이와 파란색 종이의 개수를 pair 형태로 (흰색, 파랑색) 반환하는 함수를 작성한다.
def get_paper_count(r, c, size):

    if size == 1:

        if paper[r][c]:
            return 0, 1

        else:
            return 1, 0

    checker = paper[r][c]

    for temp_r in range(size):

        for temp_c in range(size):

            if paper[r + temp_r][c + temp_c] != checker:

                result = [0, 0]

                for i in [r, r+size//2]:
                    for j in [c, c+size//2]:
                        temp_white, temp_blue = get_paper_count(i, j, size//2)
                        result[0] += temp_white
                        result[1] += temp_blue

                return result[0], result[1]

    return (0, 1) if checker else (1, 0)


# 3. 결과 값 출력
white, blue = get_paper_count(0, 0, n)
print(white)
print(blue)

