import json
from itertools import combinations_with_replacement, product


def check_number_has_enough_digits(numbers, operands):
    new_numbers = numbers

    for op in operands:
        for digit in op:
            if len(new_numbers) > 0 and digit in new_numbers:
                new_numbers = new_numbers.replace(digit, "")
            else:
                return False

    return True


def get_operands(numbers):
    operand_list_by_len = {}
    valid_operand_combinations = []
    valid_length_sums = []

    for length in range(1, len(numbers) + 1):
        operand_list_by_len[length] = [
            "".join(c) for c
            in product(numbers, repeat=length)
            if len(str(int("".join(c)))) == len("".join(c))
               and int("".join(c)) > 0  # filter out numbers starting with zero
        ]

    for length in operand_list_by_len.keys():
        valid_length_sums.extend(
            comb for comb in
            combinations_with_replacement(operand_list_by_len.keys(), r=length)
            if sum(comb) == len(numbers) and len(comb) > 1
        )

    for lengths in valid_length_sums:
        op_list = [operand_list_by_len[c] for c in lengths]
        products = [ops for ops in product(*op_list) if check_number_has_enough_digits(numbers, ops)]

        for idx, ops in enumerate(products):
            products[idx] = [int(op) for op in products[idx]]

        valid_operand_combinations.extend(products)

    return valid_operand_combinations


def build_expressions(operand_lists):
    expressions = {}
    operarators = ["+", "-", "*", "/"]

    for operands in operand_lists:
        if len(operands) - 1 == 1:
            operator_combinations = [(op, ) for op in operarators]
        else:
            operator_combinations = list(product(operarators, operarators, repeat=len(operands) - 2))

        for exp_operators in operator_combinations:
            expression = sum(zip(operands, exp_operators + (0, )), ())[:-1]
            exp_str = "".join([str(x) for x in expression])
            expressions[exp_str] = eval(exp_str)

    return expressions


if __name__ == '__main__':
    car_number = "2345"
    target = 10

    try:
        _ = int(car_number)
    except ValueError:
        print("Only integers are allowed!")
        exit(1)

    exps = build_expressions(get_operands(car_number))
    solutions = {k: v for k, v in exps.items() if v == target}

    print(json.dumps(solutions, indent=2))
