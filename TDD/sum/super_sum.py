def super_sum(*args):

    total = 0

    for item in args:
        if isinstance(item, list):

            for number in item:
                total += number

        elif isinstance(item, int):
            total += item

        elif isinstance(item, float):
            total += item

    return total