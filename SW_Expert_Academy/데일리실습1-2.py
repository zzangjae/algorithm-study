from math import ceil

post_count = int(input('게시글의 총 갯수를 입력하세요:'))
page_post = int(input('한 페이지에 필요한 게시글 수를 입력하세요:'))

print(ceil(post_count/page_post))