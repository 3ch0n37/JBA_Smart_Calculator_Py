class Calc:
    result = 0
    variables = {}

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
