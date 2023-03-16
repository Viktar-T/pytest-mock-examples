

class MockedDataset:

    def __init__(self):
        self.data = None
        self.constant_A = "mocked_constant_A"

    def load_data(self):
        self.data = 'fast data'
        return self.data

    def foo(self):
        return "mocked_foo"

def test_mocked_dataset(monkeypatch):
    dataset = MockedDataset()
    # monkeypatch.setattr('mock_examples.slow.Dataset', MockedDataset)

    # dataset = slow_dataset()
    assert dataset.constant_A == 'mocked_constant_A'
    assert dataset.load_data() == 'fast data'
    assert dataset.foo() == 'mocked_foo'