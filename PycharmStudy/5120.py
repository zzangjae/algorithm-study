import sys
sys.stdin = open("input.txt", "r")

t = int(input())


class LinkedList:

    def __init__(self, node):
        self.node = node
        self.next_node = None

    def set_next_node(self, node):
        self.next_node = LinkedList(node)

    def change_next_node(self, node):
        temp_next_node = self.next_node
        self.next_node = LinkedList(node)
        self.next_node.next_node = temp_next_node


for test_case in range(1, t + 1):
    n, m, k = map(int, input().split())
    num_lst = list(map(int, input().split()))
    start_ll = LinkedList(num_lst[0])
    temp_ll = start_ll

    for num in num_lst[1:]:

        temp_ll.set_next_node(num)
        temp_ll = temp_ll.next_node

    temp_ll = start_ll

    while k > 0:
        checker = m - 1

        while checker > 0:
            if temp_ll.next_node is not None:
                temp_ll = temp_ll.next_node
                checker -= 1
            else:
                temp_ll = start_ll
                checker -= 1

        if temp_ll.next_node is not None:
            temp_ll.change_next_node(temp_ll.node + temp_ll.next_node.start)
            temp_ll = temp_ll.next_node
        else:
            temp_ll.change_next_node(temp_ll.node + start_ll.node)
            temp_ll = temp_ll.next_node

        k -= 1

    result = []
    temp_ll = start_ll

    while temp_ll.next_node is not None:
        result.append(temp_ll.node)
        temp_ll = temp_ll.next_node

    result.append(temp_ll.node)

    if len(result) >= 10:
        print(f'#{test_case} {" ".join(map(str, result[-1:-11:-1]))}')
    else:
        print(f'#{test_case} {" ".join(map(str, result[-1::-1]))}')












