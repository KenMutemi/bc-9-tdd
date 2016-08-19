def super_sum(*args):

    total = 0

    for item in args:
        if isinstance(item, list):

            for number in item:
                total += number

        elif isinstance(item, int):
            total += item

        elif isinstance(item, float):
            for number in item:
                sum_total += number

    return float(sum_total)

    if isinstance(a, str) and isinstance(b, str) is str:
        raise TypeError

