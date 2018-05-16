
def foo(arg1: int =1):
    if hasattr(int,'arg1'):
        print('hasattr')
    else:
        print('not hasattr')
        print(arg1)


def main():
    foo()
    print(type(foo))

if __name__ == '__main__':
    main()
