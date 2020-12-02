from functools import wraps


def simple_deco(f):
    print('Decorator starts')

    def inner_func(*args, **kwargs):
        print('Inner starts')
        result = f(*args, **kwargs)
        print('Inner ends')
        return result

    print('Decorator ends')
    return inner_func


def simple_print_args(arg1, arg2):
    print(arg1)
    print(arg2)


if __name__ == '__main__':
    simple_print_args('arg1_val', 'arg2_val')
