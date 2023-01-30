n = int(input())

A, B, C, D = [[] for _ in range(4)]

for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

def make_dictionary(A, B):
    temp_dict = {}

    for num1 in A:
        for num2 in B:
            if (num1 + num2) not in temp_dict:
                temp_dict[(num1 + num2)] = 1
            else:
                temp_dict[(num1 + num2)] += 1

    return temp_dict

C_D_added_dict = make_dictionary(C, D)

result = 0

for i in A:
    for j in B:
        if -(i + j) in C_D_added_dict:
            result += C_D_added_dict[-(i + j)] 

print(result)