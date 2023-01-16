num_list = [num for num in range(1000) if not (num%2 and num%7)]
print(sum(num_list))