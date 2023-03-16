from .constants import CONSTANT_A, wrapper

CONSTANT_B = 1

def wrapper():
    return 1

def double():
    return CONSTANT_A * CONSTANT_B * 2 * wrapper()



def bar_wrapper():
    return 1

def bar(bar_wrapper):
    return 1 * bar_wrapper()


class ClassA():

    def __init__(self):
        self.a = "a"

    def foo(self):
        return "foo"

def get_class_a():
    class_a = ClassA()
    return class_a