import pytest
from main import solve


@pytest.fixture(params=[
    ([1, 1], [[-1, 1], [1, 0], [0, 1]], [2, 4, 4], 0, ([4.0, 4.0, 2.0, 0, 0], 8.0)),
    ([9, 10, 16], [[18, 15, 12], [6, 4, 8], [5, 3, 3]], [360, 192, 180], 0, ([0.0, 8.0, 20.0, 0.0, 0.0, 96.0], 400.0)),
    ([2, 3], [[1, 3], [3, 2]], [6, 6], 0, ([1.0, 2.0, 0.0, 0.0], 7.0)),
    ([2, -4, 5, -6], [[1, 4, -2, 8], [-1, 2, 3, 4]], [2, 1], 0, ([8.0, 0.0, 3.0, 0.0, 0.0, 0.0], 31.0)),
    ([1, 3], [[1, 1], [-1, 1]], [2, 4], 0, ([0.0, 2.0, 0.0, 2.0], 6.0))
])
def input_data(request):
    return request.param


def test_solve(input_data):
    c, A, b, ap, expected_result = input_data
    output, value = solve(c, A, b, ap)
    assert output == expected_result[0]
    assert value == expected_result[1]
