from lec06_ArrayStack import ArrayStack
def print_in_reverse(str):
    S = ArrayStack()

    for ch in str:
        S.push(ch)

    while (S.is_empty() == False):
        ch = S.pop()
        print(ch, end='')
    print()


def eval_postfix_exp(exp_str):
    operators = '+-*/'
    exp_lst = exp_str.split()
    args_stack = ArrayStack()
    for token in exp_lst:
        if token not in operators:
            args_stack.push(int(token))
        else:
            arg2 = args_stack.pop()
            arg1 = args_stack.pop()
            if (token == '+'):
                res = arg1 + arg2
            elif (token == '-'):
                res = arg1 - arg2
            elif (token == '*'):
                res = arg1 * arg2
            else: # token == '/'
                if arg2 == 0:
                    raise ZeroDivisionError
                else:
                    res = arg1 / arg2
            args_stack.push(res)

    return args_stack.pop()


def tokens(exp_str):
    exp_str = exp_str.strip()
    n = len(exp_str)
    i = 0

    while (i < n):
        while (exp_str[i] == ' '):
            i += 1
        if (exp_str[i] in '()+-*/'):
            yield exp_str[i]
            i += 1
        else:
            start_ind = i
            while ((i < n) and (exp_str[i].isdigit())):
                i += 1
            end_ind = i
            yield exp_str[start_ind : end_ind]


def eval_infix_exp(exp_str):
    args_stack = ArrayStack()
    ops_stack = ArrayStack()

    for token in tokens(exp_str):
        if token == '(':
            ops_stack.push(token) #1 (can be removed)
        elif token.isdigit():
            args_stack.push(int(token))
        elif token in '+-*/':
            ops_stack.push(token)
        else: # token == ')'
            arg2 = args_stack.pop()
            arg1 = args_stack.pop()
            operator = ops_stack.pop()
            ops_stack.pop() #2 popping the '(' (can be removed)
            if operator == '+':
                res = arg1 + arg2
            elif operator == '-':
                res = arg1 - arg2
            elif operator == '*':
                res = arg1 * arg2
            else:
                if arg2 == 0:
                    raise ZeroDivisionError
                else:
                    res = arg1 / arg2
            args_stack.push(res)

    return args_stack.pop()

def eval_infix_exp2(exp_str):
    exp_stack = ArrayStack()

    for token in tokens(exp_str):
        if token == '(':
            exp_stack.push(token) #1 (can be removed)
        elif token.isdigit():
            exp_stack.push(int(token))
        elif token in '+-*/':
            exp_stack.push(token)
        else: # token == ')'
            arg2 = exp_stack.pop()
            operator = exp_stack.pop()
            arg1 = exp_stack.pop()
            exp_stack.pop() #2 popping the '(' (can be removed)
            if operator == '+':
                res = arg1 + arg2
            elif operator == '-':
                res = arg1 - arg2
            elif operator == '*':
                res = arg1 * arg2
            else:
                if arg2 == 0:
                    raise ZeroDivisionError
                else:
                    res = arg1 / arg2
            exp_stack.push(res)

    return exp_stack.pop()

def infix_to_postfix(expression):
    ops_stack = ArrayStack()
    postfix_exp_list = []

    for token in tokens(expression):
        if token.isdigit():
            postfix_exp_list.append(token)
        elif token == '(':
            ops_stack.push(token)
        elif token in '+-*/':
            ops_stack.push(token)
        else:
            operator = ops_stack.pop()
            ops_stack.pop() # popping the '('
            postfix_exp_list.append(operator)

    return ' '.join(postfix_exp_list)


def is_matched(expr):
    lefty = '({['
    righty = ')}]'

    S = ArrayStack()

    for token in expr:
        if token in lefty:
            S.push(token)
        elif token in righty:
            if S.is_empty( ):
                return False
            from_S = S.top()
            if (righty.index(token) == lefty.index(from_S)):
                S.pop()
            else:
                return False
        else:
            raise ValueError

    return S.is_empty()


#print(eval_infix_exp2('(1 + (((2 * (21 - (3 + 4))) + 4) - 5))'))
#print(infix_to_postfix('(1 + (((2 * (21 - (3 + 4))) + 4) - 5))'))
print(eval_postfix_exp('2 3 4 + 3 * 4 6 - + *'))
