from calc import Calc, is_number
from collections import deque
import re


def menu(command):
    if command == '/exit':
        return False
    elif command == '/help':
        return 'The program is a simple calculator, terms and operations are separated by spaces.\n' \
               'Supported operations: adding, subtracting, multiplication and division.\n' \
               'Grouping using brackets is also supported.\n'
    else:
        return 'Unknown command'


def main():
    expression = ''
    calculator = Calc()

    while expression != '/exit':
        expression = input()
        if expression == '':
            continue
        if expression[0] == '/':
            message = menu(expression)
            if message:
                print(message)
            continue
        if '=' in expression:
            r = calculator.assignment(expression)
            if r is not True:
                print(r)
        else:
            factor = 1
            result = 0
            expression = calculator.infix_to_postfix(expression)
            if not expression:
                print('Invalid expression')
                continue
            if len(expression) == 1 and not is_number(expression[0]):
                print(calculator.get_value(expression[0]))
            else:
                result = calculator.evaluate()
                if result is False:
                    print('Invalid expression')
                else:
                    print(result)
                """
                for index, term in enumerate(expression):
                    if index % 2 == 0:
                        if is_number(term):
                            result += factor * int(term)
                        elif term.isalnum():
                            n = calculator.get_value(term)
                            if not is_number(n):
                                print(n)
                                result = False
                                break
                            else:
                                result += factor * int(n)
                        else:
                            print('Invalid expression')
                            result = False
                            break
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
                """

    print('Bye!')


if __name__ == '__main__':
    main()
