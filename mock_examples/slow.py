import time


def api_call():
    time.sleep(3)
    return 9


class Dataset:

    def __init__(self):
        self.data = None
        self.constant_A = "constant_A"
        self.constant_B = "constant_B"

    def load_data(self):
        time.sleep(4)
        self.data = 'slow data'
        return self.data

    def foo(self):
        time.sleep(3)
        return "foo"
