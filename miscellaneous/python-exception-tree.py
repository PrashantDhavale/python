def print_exception_tree(this, nest=0):
    if nest > 1:
        print("   |" * (nest - 1), end="")
    if nest > 0:
        print("   +---", end="")

    print(this.__name__)

    for subclass in this.__subclasses__():
        print_exception_tree(subclass, nest + 1)


print_exception_tree(BaseException)
