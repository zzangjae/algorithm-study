text_input = input()
text = list(text_input)

def get_equation(num_list):
    
    if num_list.count('[') != num_list.count(']') or num_list.count('(') != num_list.count(')'):
        return 0 

    temp_list = []

    for idx in range(len(text)-1):
        if text[idx] == '(' and (text[idx+1] == '(' or text[idx+1] == '['):
            temp_list.append('2*(')
        elif text[idx] == '[' and (text[idx+1] == '(' or text[idx+1] == '['):
            temp_list.append('3*(')
        elif text[idx] == '(' and text[idx+1] == ')':
            temp_list.append('2')
        elif text[idx] == '[' and text[idx+1] == ']':
            temp_list.append('3')
        elif (text[idx] == ')' or text[idx] == ']') and ((text[idx+1] == ')' or text[idx+1] == ']')):
            temp_list.append(')')
        elif (text[idx] == ')' or text[idx] == ']') and ((text[idx+1] == '(' or text[idx+1] == '[')):
            temp_list.append('+')
        else:
            return 0

    return temp_list
    
try:
    print(eval(''.join(get_equation(text))))
except:
    print(0)


    
