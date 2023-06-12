def find_page(l, r, page, count):
    c = int((l+r)/2)

    if c == page:
        return count
    elif c < page < r:
        return find_page(c, r, page, count + 1)
    elif l < page < c:
        return find_page(l, c, page, count+1)

test_case = int(input())

for case in range(test_case):
    p, pa, pb = map(int, input().split())

    if find_page(1, p, pa, 0) > find_page(1, p, pb, 0):
        print(f'#{case+1} B')
    elif find_page(1, p, pa, 0) < find_page(1, p, pb, 0):
        print(f'#{case+1} A')
    elif find_page(1, p, pa, 0) == find_page(1, p, pb, 0):
        print(f'#{case+1} 0')
    