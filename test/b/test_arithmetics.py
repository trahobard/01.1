import pytest

from unittest.mock import patch
from io import StringIO

from test.common.mockit import mock, mock_print
from test.common.context import get_integer, get_float


@pytest.mark.parametrize(
    ['x', 'y', 'z', 'answers'],
    [
        (10, 3, 0.5, ['10 3 0.5', 13.5, 15.0, 5, 20.0, 20.0, 1, 1.7320508075688772, 109044078.609375, '0.50000'])
    ]
)
def test_arithmetics(x, y, z, answers, step):
    with mock(get_integer).returns_many(x, y), mock(get_float).returns(z), \
            mock_print() as output:
        import tasks.b.arithmetics
        result = [line for line in output.getvalue().split('\n') if line.strip() != '']

        if step is None:
            assert len(result) == len(answers)  # Выведено неверное количество строк
            for rec, exp in zip(result, answers):
                assert rec == str(exp)  # Выведен неверный результат
        else:
            step -= 1
            assert len(result) > step  # Выведено меньше строк, чем номер пункта
            assert result[step] == str(answers[step])  # Выведен неверный результат
