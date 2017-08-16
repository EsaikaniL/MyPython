def someFunction():
    x=input("Enter x")
    y=input("Enter y")
    z=(x+y)
    a=z%10
    print'Addtion of value is: ',z
    print'modulo value is: ',a

def add(a,b):
    e=a+b
    return e


def main():
    """a=input("Enter a value: ")
    b=input("Enter b value: ")"""
    print add(a=input("Enter a value: "),b=input("Enter b value"))


if __name__ == "__main__":
    main()
    someFunction()
