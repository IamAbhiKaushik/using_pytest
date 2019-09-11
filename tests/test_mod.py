def func(x):
    return x + 1

# Function written with name starting from format test_.py will be executed automatically if not mentioned


def test_func():
    assert func(3) == 4
