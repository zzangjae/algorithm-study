string = input()
string_length = len(string)

if string_length % 2:
    print(string[string_length//2])
else:
    print(string[string_length//2 - 1 : string_length//2 + 1])


