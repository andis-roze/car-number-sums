import itertools
import json


def check_all_digits_used_once(numbers, operands):
    new_numbers = numbers

    for op in operands:
        for digit in op:
            if len(new_numbers) > 0 and digit in new_numbers:
                new_numbers = new_numbers.replace(digit, "")
            else:
                return False

    return True and (len(new_numbers) == 0 or int(new_numbers) == 0)


def get_operands(number):
    operand_list_by_len = {}
    valid_operand_combinations = []
    valid_length_sums = []

    for length in range(1, len(number) + 1):
        operand_list_by_len[length] = [
            "".join(c)
            for c in itertools.product(number, repeat=length)
            if len(str(int("".join(c)))) == len("".join(c))
            and int("".join(c)) > 0  # filter out numbers starting with zero
        ]

    for length in operand_list_by_len.keys():
        valid_length_sums.extend(
            comb
            for comb in itertools.combinations_with_replacement(
                operand_list_by_len.keys(), r=length
            )
            if sum(comb) <= len(number)
        )

    for lengths in valid_length_sums:
        op_list = [operand_list_by_len[c] for c in lengths]
        products = [
            ops
            for ops in itertools.product(*op_list)
            if check_all_digits_used_once(number, ops)
        ]

        for idx, ops in enumerate(products):
            products[idx] = [int(op) for op in products[idx]]

        valid_operand_combinations.extend(products)

    return valid_operand_combinations


def build_expressions(operand_lists):
    expressions = {}
    operators = ["+", "-", "*", "/"]

    for operands in operand_lists:
        if len(operands) < 2:
            operator_combinations = [(op,) for op in operators]
        else:
            operator_combinations = list(
                itertools.product(operators, operators, repeat=len(operands) - 2)
            )

        for exp_operators in operator_combinations:
            expression = sum(zip(operands, exp_operators + (0,)), ())[:-1]
            exp_str = "".join([str(x) for x in expression])
            expressions[exp_str] = eval(exp_str)

    return expressions


def get_expressions_for_number(number):
    return build_expressions(get_operands(number))


def get_expressions_reaching_target(number, target_value):
    return {
        k: v for k, v in get_expressions_for_number(number).items() if v == target_value
    }


if __name__ == "__main__":
    digits = "012345678"
    number_len = 4
    target = 10
    print_all_solutions = False

    for car_number_tuple in itertools.combinations(digits, r=number_len):
        car_number = "".join(car_number_tuple)
        # car_number = "0138"
        solutions = get_expressions_reaching_target(car_number, target)

        print(f"Number {car_number} has {len(solutions.keys())} solutions")

        if print_all_solutions:
            print(json.dumps(solutions, indent=2))
