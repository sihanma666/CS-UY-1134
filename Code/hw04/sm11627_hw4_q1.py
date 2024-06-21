# implement an interpreter-like postfix calculator. Your program should repeatedly:
# > print a prompt to the user. The prompst should be: '-->'BaseException
# > read an expression from the user 
# > evaluate that expression
# > print the result

# 1) artihmetic expressions are given in postfix notation. The tokens of the
# expression are separated by a space 

# 2) assignment expressions are expression of the form:
# variable_name = arithmetic_expression
# When evaluated, it first evaluates the arithmetic_expression (given in postfix
# notation), and then it associates that value with variable_name (in a data structure of choice)
# > value of assignment expession is name of variable being assigned
# > assume that variable_name, the '=' symbol, and the arithmetic_expression
# are separated by a space 

from ArrayStack import ArrayStack

variable_names = []
variable_values = []

def evaluate_postfix(lst):
    s = ArrayStack()

    for i in len(lst): #N
        x=lst[i]

        if (is_floatnum(x)):
            s.push(float(x))
        elif (x == "-"):
            item2 = s.pop()
            item1 = s.pop()
            s.push(item1-item2)
        elif (x == "+"):
            item2 = s.pop()
            item1 = s.pop()
            s.push(item1+item2)
        elif (x == "/"):
            item2 = s.pop()
            item1 = s.pop()
            s.push(item1/item2)
        elif (x == "*"):
            item2 = s.pop()
            item1 = s.pop()
            s.push(item1*item2)
        else:
            value = variable_values[i]
            s.push(value)

    return s.top()

def is_floatnum(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

def main():
    exit = False
    while(exit != True):
        user_input = input('--> ')
        if user_input == 'done()':
            exit = True
        else:
            lst = [x for x in user_input] #N
            if ((len(lst) >= 2) and (lst[1] == '=')): #input: 'x=...'
                variable_name = lst[0]
                variable_value = evaluate_postfix(lst[2:])
                variable_names.append(variable_name)
                variable_values.append(variable_value)
                print(variable_value)
            else:
                output = evaluate_postfix(lst)
                if (output == int(output)):
                    print(int(output))
                else:
                    print(output)

main()


