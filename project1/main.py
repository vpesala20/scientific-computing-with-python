def arithmetic_arranger(problems, show_answers=False):
    # Check if too many problems
    if len(problems) > 5:
        return "Error: Too many problems."

    first_operands = []
    second_operands = []
    operators = []
    results = []

    # Parse and validate each problem
    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid problem format."

        first, operator, second = parts

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not first.isdigit() or not second.isdigit():
            return "Error: Numbers must only contain digits."

        if len(first) > 4 or len(second) > 4:
            return "Error: Numbers cannot be more than four digits."

        first_operands.append(first)
        second_operands.append(second)
        operators.append(operator)

        # Calculate result for optional display
        if operator == '+':
            results.append(str(int(first) + int(second)))
        else:
            results.append(str(int(first) - int(second)))

    # Build arranged lines
    arranged_first_line = []
    arranged_second_line = []
    arranged_dashes = []
    arranged_results = []

    for i in range(len(problems)):
        first = first_operands[i]
        second = second_operands[i]
        operator = operators[i]
        result = results[i]

        width = max(len(first), len(second)) + 2  # operator + space

        arranged_first_line.append(first.rjust(width))
        arranged_second_line.append(operator + ' ' + second.rjust(width - 2))
        arranged_dashes.append('-' * width)
        arranged_results.append(result.rjust(width))

    first_line = '    '.join(arranged_first_line)
    second_line = '    '.join(arranged_second_line)
    dashes_line = '    '.join(arranged_dashes)
    results_line = '    '.join(arranged_results)

    if show_answers:
        return f"{first_line}\n{second_line}\n{dashes_line}\n{results_line}"
    else:
        return f"{first_line}\n{second_line}\n{dashes_line}"


# Example usage
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print()
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))