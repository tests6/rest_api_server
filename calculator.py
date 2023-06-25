def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def evaluate_rpn(expression: list[str]) -> float:
    stack = []

    for token in expression:
        if token.isdigit():
            stack.append(int(token))
        elif is_float(token):
            stack.append(float(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()

            if token == "+":
                result = operand1 + operand2
            elif token == "-":
                result = operand1 - operand2
            elif token == "*":
                result = operand1 * operand2
            elif token == "/":
                result = operand1 / operand2
            else:
                raise ValueError("Invalid operator: " + token)

            stack.append(result)

    return stack[0]
