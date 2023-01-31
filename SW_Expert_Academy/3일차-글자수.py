t = int(input())

for iteration in range(t):
    str1 = input()
    str2 = input()
    str1_dict = {}
    str2_dict = {}

    for chr in str2:
        if chr in str2_dict:
            str2_dict[chr] += 1
        else:
            str2_dict[chr] = 1
    
    for chr in str1:
        str1_dict[chr] = str2_dict[chr]

    print(f'#{iteration+1} {max(str1_dict.values())}')
