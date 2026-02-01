def funcOne():
    """
    Entry function in the call chain.

    Logic:
    1. Calls funcTwo(), transferring control to the next stack frame.
    2. Prints "One" after funcTwo() completes and returns.
    """
    funcTwo()
    print("One")


def funcTwo():
    """
    Intermediate function in the call chain.

    Logic:
    1. Calls funcThree(), pushing a new stack frame.
    2. Prints "Two" after funcThree() completes and returns.
    """
    funcThree()
    print("Two")


def funcThree():
    """
    Leaf function in the call chain.

    Logic:
    1. Executes a print statement.
    2. Returns implicitly (None).
    """
    print("Three")


# ---------------------------
# Function Call Stack Demo
# ---------------------------

funcOne()


def factorial(n):
    """
    Compute factorial of a positive integer using recursion.

    Logic:
    1. Base case: if n == 1, return 1.
    2. Recursive case: n * factorial(n - 1).
    """
    if n == 1:
        return n
    return n * factorial(n - 1)


# ---------------------------
# Recursion Demo
# ---------------------------

print(factorial(4))
