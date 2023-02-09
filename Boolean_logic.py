class BooleanExpression:
    def __init__(self, expression):
        self.expression = expression
        self.variables = {}

    def evaluate(self):
        return self.eval_expression(self.expression)

    def eval_expression(self, expression):
        if expression[0] == '!':
            return not self.eval_expression(expression[1:])
        elif expression[0] == '(':
            return self.eval_expression(expression[1:-1])
        elif expression in ['T', 'F']:
            return expression == 'T'
        else:
            return self.variables[expression]

    def set_variable(self, name, value):
        self.variables[name] = value


def main():
    while True:
        expression = input("λ> ")
        if expression == 'exit':
            break

        if expression.startswith("let "):
            parts = expression.split("=")
            name = parts[0][4:].strip()
            value = parts[1].strip()
            if value in ['T', 'F']:
                b = BooleanExpression("")
                b.set_variable(name, value == 'T')
                print("{}: {}".format(name, value))
            else:
                b = BooleanExpression(value)
                b.set_variable(name, b.evaluate())
                print("{}: {}".format(name, b.variables[name]))
        else:
            b = BooleanExpression(expression)
            result = b.evaluate()
            print(result)


if __name__ == '__main__':
    main()
