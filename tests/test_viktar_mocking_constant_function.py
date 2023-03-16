from unittest.mock import MagicMock

import mock_examples.functions
from mock_examples.functions import double, bar, get_class_a
# from mock_examples.slow import api_call
from mock_examples.main import slow_function, slow_dataset
from mock_examples.slow import Dataset

def test_mocking_constant_a(mocker, monkeypatch):
    # mocker.patch.object(mock_examples.functions, "CONSTANT_A", 10)
    # mock_wrapper = MagicMock()
    # mock_wrapper.return_value.wrapper.return_value = 1000

    ################################################
    monkeypatch.setattr(mock_examples.functions, "CONSTANT_A", 5)
    monkeypatch.setattr(mock_examples.functions, "CONSTANT_B", 2)
    monkeypatch.setattr(mock_examples.functions, "wrapper", lambda: 10)
    #################################################
    expected = 200
    actual = double()

    assert expected == actual

def test_mocking_bar(mocker, monkeypatch):

    # mock_wrapper = MagicMock(return_value=5)
                # or
    mock_wrapper = MagicMock()
    mock_wrapper.return_value = 5

    expected = 5
    actual = bar(mock_wrapper)

    assert expected == actual


def test_mocking_class_a(monkeypatch):
    mock_class = MagicMock()
    mock_class.return_value.foo.return_value = "mocked_foo"
    mock_class.return_value.a = "mocked_a"

    monkeypatch.setattr(mock_examples.functions, "ClassA", mock_class)

    class_a = get_class_a()
    assert class_a.foo() == "mocked_foo"
    assert class_a.a == "mocked_a"


def test_mocking_slow_function(mocker, monkeypatch):
    def get_response():
        return 9
    # mocker.patch.object(mock_examples.functions, "CONSTANT_A", 10)
    # mocker.patch.object(mock_examples.main, "api_call", lambda: 9)
    # monkeypatch.setattr(mock_examples.main, "api_call", lambda: 9)
    monkeypatch.setattr(mock_examples.main, "api_call", get_response)

    expected = 9
    actual = slow_function()

    assert expected == actual

#################################################
#################################################
#################################################
class MockedDataset:

    def __init__(self):
        self.data = None
        self.constant_A = "mocked_constant_A"
        self.constant_B = "mocked_constant_B"

    def load_data(self):
        self.data = 'fast data'
        return self.data

    def foo(self):
        return "mocked_foo"

def test_mocked_dataset(monkeypatch):

    # dataset = MockedDataset()
    monkeypatch.setattr('mock_examples.main.Dataset', MockedDataset)

    dataset = slow_dataset()
    assert dataset.constant_A == 'mocked_constant_A'
    assert dataset.constant_B == 'mocked_constant_B'
    assert dataset.load_data() == 'fast data'
    assert dataset.foo() == 'mocked_foo'

#################################################
#################################################
#################################################

#################################################
#################################################
#################################################

def test_mocked_dataset_magic_mock(monkeypatch):
    magic_mock = MagicMock()
    magic_mock.return_value.constant_A = 'mocked_constant_A'
    magic_mock.return_value.constant_B = 'mocked_constant_B'
    magic_mock.return_value.load_data.return_value = 'fast data'
    magic_mock.foo.return_value = 'mocked_foo'

    monkeypatch.setattr('mock_examples.main.Dataset', magic_mock)

    dataset = slow_dataset()

    assert dataset.constant_A == 'mocked_constant_A'
    assert dataset.constant_B == 'mocked_constant_B'
    assert dataset.load_data() == 'fast data'
    # assert dataset.foo() == 'mocked_foo'

#################################################
#################################################
#################################################

def test_dataset(monkeypatch):
    dataset = Dataset()
    # monkeypatch.setattr('mock_examples.slow.Dataset.constant_A', 'mocked_constant_A')
    monkeypatch.setattr(dataset, "constant_A", 'mocked_constant_A')


    def mocked_foo(*args, **kwargs):
        return "mocked_foo"

    monkeypatch.setattr('mock_examples.slow.Dataset.foo', mocked_foo)
    actual_foo = dataset.foo()

    def mocked_load_data(*args, **kwargs):
        return "mocked_load_data"

    monkeypatch.setattr('mock_examples.slow.Dataset.load_data', mocked_load_data)
    actual_load_data = dataset.load_data()

    assert dataset.constant_A == 'mocked_constant_A'
    assert actual_foo == "mocked_foo"
    assert actual_load_data == "mocked_load_data"


##### ERROR ######
# def test_slow_db(mocker, monkeypatch):
#     load_data_expected_res = "viktar_data"
#
#     def mocked_load(*args, **kwargs):
#         return "viktar_data"
#
#     # monkeypatch.setattr(mock_examples.main.Dataset, "load_data", lambda: "viktar_data")
#     # mocker.patch("mock_examples.main.Dataset.load_data", mocked_load)
#
#     monkeypatch.setattr(mock_examples.main.Dataset, "load_data", mocked_load)
#     # monkeypatch.setattr(mock_examples.main.slow_dataset.dataset, "constant_A", "constant_mocked")
#
#     mock_constant_a = MagicMock()
#     mock_constant_a.constant_A = "constant_mocked"
#
#     mocker.patch.object(mock_examples.main.slow_dataset, "constant_A", mock_constant_a)
#
#     dataset_obj = slow_dataset()
#
#     load_data_actual_res = dataset_obj.load_data()
#     assert load_data_expected_res == load_data_actual_res
#     assert dataset_obj.constant_A == "constant_mocked"



# class MockedDataset:
#     def __init__(self):
#         self.data = None
#
#     def load_data(self):
#         self.data = "viktar_data"

# def test_slow_db(monkeypatch):
#     monkeypatch.setattr(mock_examples.main, "Dataset", MockedDataset)
#     expected_res = "viktar_data"
#     actual_res = slow_dataset()
#
#     assert expected_res == actual_res
