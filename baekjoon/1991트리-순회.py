tree = {}
n = int(input())

for _ in range(n):
    x, y, z = input().split()
    tree[x] = [y, z]

def preorder_traversal(x):

    if x == '.':
        return None
    
    print(x, end='')

    for child in tree[x]:
        preorder_traversal(child)

    return None

def inorder_traversal(x):

    if x == '.':
        return ''

    return inorder_traversal(tree[x][0]) + x + inorder_traversal(tree[x][1])

def postorder_traversal(x):

    if x == '.':
        return ''

    return postorder_traversal(tree[x][0]) + postorder_traversal(tree[x][1]) + x


preorder_traversal('A')
print()
print(inorder_traversal('A'))
print(postorder_traversal('A'))
