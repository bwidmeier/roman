def parse(numeral_string):
    if not numeral_string:
        raise Exception('must pass a non-empty string as input')

    accumulation = 0
    last_value = 0
    for numeral in numeral_string:
        if last_value == 0:
            # initial case and also case following a subtraction
            last_value = _translate(numeral)
            continue

        current_value = _translate(numeral)

        if last_value < current_value:
            accumulation += current_value - last_value
            last_value = 0
            continue

        accumulation += last_value
        last_value = current_value

    accumulation += last_value
    return accumulation


def _translate(numeral):
    if numeral == 'I':
        return 1
    elif numeral == 'V':
        return 5
    elif numeral == 'X':
        return 10
    elif numeral == 'L':
        return 50
    elif numeral == 'C':
        return 100
    elif numeral == 'D':
        return 500
    elif numeral == 'M':
        return 1000
    else:
        raise Exception(f'input string contained invalid numeral: {numeral}')
