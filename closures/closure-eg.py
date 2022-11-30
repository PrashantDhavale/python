def greeter(prefix):
    def greet(name):
        print(f"{prefix} {name}")

    return greet


hello = greeter("hello,")
goodbye = greeter("goodbye,")

hello("Rohan")
goodbye("Yashika")
