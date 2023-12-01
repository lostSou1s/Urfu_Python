def validate_args(func):
    def inner(*args):
        if len(args) < 1:
            return "Not enough arguments"
        elif len(args) > 1:
            return "Too many arguments"
        elif args[0] % 1 != 0:
            return "Wrong types"
        elif args[0] < 0:
            return "Negative argument"
        return func(*args)
    return inner


@validate_args
def calculate(num):
    return num * num

print(calculate(-1))
