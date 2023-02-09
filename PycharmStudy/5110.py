import sys
sys.stdin = open("input.txt", "r")

t = int(input())


class LinkedList:

    def __init__(self, node):
        self.node = node
        self.next_node = None

    def get(self, node):
        self.next_node = LinkedList(node)

    def add(self, node_instance):
        next_instance = self.next_node
        self.next_node = node_instance

        while node_instance.next_node is not None:
            node_instance = node_instance.next_node

        node_instance.next_node = next_instance


for iteration in range(t):

    n, m = map(int, input().split())
    num_lst = [list(map(int, input().split())) for _ in range(m)]
    instance_lst = []

    for lst in num_lst:
        temp_instance = LinkedList(lst[0])
        instance_lst.append(temp_instance)

        for num in lst[1:]:
            temp_instance.get(num)
            temp_instance = temp_instance.next_node

    for instance in instance_lst[1:]:

        temp_instance = instance_lst[0]

        if temp_instance.node > instance.node:
            instance_lst[0] = instance
            while instance.next_node is not None:
                instance = instance.next_node
            instance.add(temp_instance)
            continue

        while True:

            if temp_instance.next_node is None:
                temp_instance.add(instance)
                break

            if temp_instance.next_node.node > instance.node:
                temp_instance.add(instance)
                break

            temp_instance = temp_instance.next_node

    result = []
    temp_instance = instance_lst[0]
    result.append(temp_instance.node)

    while True:
        temp_instance = temp_instance.next_node
        result.append(temp_instance.node)
        if temp_instance.next_node is None:
            break

    if len(result) >= 10:
        print(f'#{iteration + 1} {" ".join(map(str, result[-1: -11: -1]))}')
    else:
        print(f'#{iteration + 1} {" ".join(map(str, result[-1:: -1]))}')

