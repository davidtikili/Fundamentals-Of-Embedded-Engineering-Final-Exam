def trc1(func):
    def decorator(*args, **kwargs):
        args_str = ' '.join(str(arg) for arg in args)
        print(f"Calling {func} on argument {args_str}")
        return func(*args, **kwargs)
    return decorator

@trc1
def sqr(x):
    return x * x

@trc1
def sum_sqr(n):
    return sum(sqr(i) for i in range(1, n+1))

def main():
    print(sqr(3))
    print(sum_sqr(3))

main()
