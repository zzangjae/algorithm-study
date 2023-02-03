import sys

sys.stdin = open("input.txt", "r")

T = int(input())


class KangarooTree:

    def __init__(self, left=None, right=None, next_tree=None):
        self.kangaroo_num = 1
        self.right = right
        self.left = left
        self.next_tree = next_tree


def get_tree(tree, left, right):
    if right < tree.left or tree.right < left:
        tree.left = left
        tree.right = right
        tree.kangaroo_num = 1
        tree.next_tree = None

    elif tree.left <= left and right <= tree.right:
        tree.left, left = left, tree.left
        tree.right, right = right, tree.right
        tree.kangaroo_num += 1

    elif tree.left <= left and tree.right < right:
        tree.left, left = left, tree.left
        if tree.next_tree is None:
            tree.kangaroo_num += 1
            tree.next_tree = KangarooTree(tree.right + 1, right)
        else:
            tree.kangaroo_num += 1
            get_tree(tree.next_tree, tree.right + 1, right)

    elif right <= tree.right and left < tree.left:
        tree.right, right = right, tree.right
        if tree.next_tree is None:
            tree.kangaroo_num += 1
            tree.next_tree = KangarooTree(left, tree.left)
        else:
            tree.kangaroo_num += 1
            get_tree(tree.next_tree, left, tree.left)

    elif left < tree.left and tree.right < right:
        if tree.next_tree is None:
            tree.kangaroo_num += 1
            tree.next_tree = KangarooTree(left, right)
        else:
            tree.kangaroo_num += 1
            get_tree(tree.next_tree, left, right)


def get_into_tree(tree, left, right):
    if right < tree.left or tree.right < left:
        return 0
    else:
        return tree.kangaroo_num


def find_max_kangaroo(tree_lst, camera_left, camera_right):
    max_kangaroo = 0
    count = 0

    for tree in tree_lst:
        temp_tree = tree
        while True:
            temp_num = get_into_tree(temp_tree, camera_left, camera_right)
            if temp_num != 0:
                count += temp_num
                if max_kangaroo < count:
                    max_kangaroo = count
                    break
            else:
                count = 0
                if temp_tree.next_tree is not None:
                    temp_tree = temp_tree.next_tree
                    continue
                else:
                    break
            break

    return max_kangaroo


for iteration in range(T):
    n, m = map(int, input().split())
    kangaroo_tree_lst = []
    kangaroo_val_lst = []
    result = 0

    a, b = map(int, input().split())
    kangaroo_tree_lst.append(KangarooTree(a, b))

    for _ in range(n - 1):
        a, b = map(int, input().split())
        if b < kangaroo_tree_lst[-1].left or kangaroo_tree_lst[-1].right < a:
            kangaroo_tree_lst.append(KangarooTree(a, b))
        else:
            get_tree(kangaroo_tree_lst[-1], a, b)

    for idx in range(1, m + 1):
        l, r = map(int, input().split())

        result += find_max_kangaroo(kangaroo_tree_lst, l, r) * idx

    print(f'#{iteration + 1} {result}')

