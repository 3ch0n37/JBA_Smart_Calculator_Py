# write your code here
def is_number(x):
    try:
        int(x)
    except ValueError:
        return False
    return True

def menu(command):
    if command == '/exit':
        return False
    elif command == '/help':
        return 'The program is a simple calculator, terms and operations are separated by spaces.'
    else:
        return 'Unknown command'


def main():
    expression = None

    while expression != '/exit':
        expression = input()
        if expression == '':
            continue
        if expression[0] == '/':
            message = menu(expression)
            if message:
                print(message)
            continue
        factor = 1
        result = 0
        expression = expression.split()
        if len(expression) % 2 == 0:
            print('Invalid exception')
            continue
        for index, term in enumerate(expression):
            if index % 2 == 0:
                if not is_number(term):
                    print('Invalid expression')
                    result = False
                else:
                    result += factor * int(term)
            else:
                if '-' in term and not is_number(term):
                    if len(term) % 2 == 0 and '+' not in term:
                        factor = 1
                    else:
                        factor = -1
                elif '+' in term:
                    factor = 1
        if result is not False:
            print(result)

    print('Bye!')


if __name__ == '__main__':
    main()
