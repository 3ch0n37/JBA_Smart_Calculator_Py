import re
from collections import deque


def is_number(x):
    try:
        int(x)
    except ValueError:
        return False
    return True


class Calc:

    def __init__(self):
        self.expression = None
        self.result = 0
        self.variables = {}

    def addition(self, factor, number):
        self.result += factor * number

    def assignment(self, expression):
        expression = expression.replace(' ', '')
        expression = expression.split('=')
        if len(expression) != 2:
            return 'Invalid assignment'
        name, value = expression
        if not name.isalpha():
            return 'Invalid identifier'
        if value.isalpha():
            value = self.get_value(value)
        try:
            value = int(value)
        except ValueError:
            return 'Invalid assignment'
        self.variables[name] = value
        return True

    def get_value(self, name):
        if not name.isalpha():
            return 'Invalid identifier'
        if name not in self.variables:
            return 'Unknown variable'
        return self.variables[name]

    def infix_to_postfix(self, expr):
        expr = re.findall(r'-?\d+|\++|-+|\*+|/+|[a-z][a-z1-9]*|\(|\)', expr)
        postfix = deque()
        operators = deque()
        last = ''
        for term in expr:
            if term.isalnum() or '-' in term and is_number(term):
                postfix.append(term)
            else:
                if len(term) > 1:
                    if re.match('[*/()]', term):
                        return False
                    elif '-' in term:
                        if len(term) % 2 == 0:
                            term = '+'
                        else:
                            term = '-'
                    elif '+' in term:
                        term = '+'
                if len(operators) == 0 or operators[-1] == '(':
                    operators.append(term)
                elif len(operators) > 0:
                    if term in '*/' and operators[-1] in '+-':
                        operators.append(term)
                    elif term in '+-' and operators[-1] in '*/' or term in '+-' and operators[-1] in '+-' \
                            or term in '*/' and operators[-1] in '*/':
                        while len(operators) and operators[-1] != '(':
                            postfix.append(operators.pop())
                        operators.append(term)
                    elif term == '(':
                        operators.append(term)
                    elif term == ')':
                        if '(' not in operators:
                            return False
                        while len(operators) and operators[-1] != '(':
                            postfix.append(operators.pop())
                        if operators[-1] == '(':
                            operators.pop()

        if '(' in operators:
            return False

        while len(operators):
            postfix.append(operators.pop())
        self.expression = postfix
        return postfix

    def evaluate(self):
        result = deque()
        if self.expression is None:
            return False
        while len(self.expression):
            term = self.expression.popleft()
            if term.isalpha() or is_number(term):
                if term.isalpha():
                    term = self.get_value(term)
                if not is_number(term):
                    return False
                result.appendleft(term)
            elif term in '+-*/':
                b = int(result.popleft())
                a = int(result.popleft())
                if term == '+':
                    result.appendleft(a + b)
                elif term == '-':
                    result.appendleft(a - b)
                elif term == '*':
                    result.appendleft(a * b)
                elif term == '/':
                    if b == 0:
                        return False
                    result.appendleft(a / b)
        if len(result) > 1:
            return False
        self.expression = None
        return result.pop()
