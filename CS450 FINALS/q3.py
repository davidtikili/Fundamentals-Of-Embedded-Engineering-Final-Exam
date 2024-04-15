def deep_rvrs(tup):
    if isinstance(tup, tuple):
        return tuple(deep_rvrs(item) for item in reversed(tup))
    else:
        return tup

def main():
    a = (11, 12, 13, 14)
    print(deep_rvrs(a))  

    tpl = (11, (12, (13, 113), 14), 15)
    print(deep_rvrs(tpl))  

main()