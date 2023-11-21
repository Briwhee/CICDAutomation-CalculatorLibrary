# Unit tests for the calculator library

import calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(2,2)

    def test_subtraction(self):
        assert 2 == calculator.subtract(4,2)


# test with "pytest -v --cov" this will test any file with the prefix test 
# -v gives a clean look, 
# --cov gives a code coverage report