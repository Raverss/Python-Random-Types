import os
import sys
from random import randint, uniform

# Add the parent directory to sys.path to import the module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from tasadofi import random_number as rnd


class TestRandomIntUniform:
    a = -5
    b = 5
    reps = 1000

    def test_int_eq(self):
        number = rnd.RndInt('randint', self.a, self.b)
        for _ in range(self.reps):
            assert self.a <= number <= self.b, f"Random number is not in the expected range [{self.a}, {self.b}]"

    def test_int_arithmetics(self):
        number = rnd.RndInt('randint', self.a, self.b)

        for _ in range(self.reps):
            result = number + 1
            assert (
                self.a + 1 <= result <= self.b + 1
            ), f"Result {result} is not in the expected range [{self.a + 1}, {self.b + 1}]"

            result = number - 1
            assert (
                self.a - 1 <= result <= self.b - 1
            ), f"Result {result} is not in the expected range [{self.a - 1}, {self.b - 1}]"

            result = number * 2
            assert (
                2 * self.a <= result <= 2 * self.b
            ), f"Result {result} is not in the expected range [{2 * self.a}, {2 * self.b}]"

            result = number / 2
            assert (
                self.a / 2 <= result <= self.b / 2
            ), f"Result {result} is not in the expected range [{self.a / 2}, {self.b / 2}]"

    def test_int_type(self):
        number = rnd.RndInt('randint', self.a, self.b)
        assert isinstance(number, int), f"Expected int, got {type(number)}"

    def test_int_samplers(self):
        # test str sampler with args
        number = rnd.RndInt('randint', self.a, self.b)
        assert self.a <= number <= self.b, f"Random number is not in the expected range [{self.a}, {self.b}]"

        # test str sampler with kwargs
        number = rnd.RndInt('randint', a=self.a, b=self.b)
        assert self.a <= number <= self.b, f"Random number is not in the expected range [{self.a}, {self.b}]"

        # test callable sampler with args
        number = rnd.RndInt(randint, self.a, self.b)
        assert self.a <= number <= self.b, f"Random number is not in the expected range [{self.a}, {self.b}]"

        # test callable sampler with kwargs
        number = rnd.RndInt(randint, a=self.a, b=self.b)
        assert self.a <= number <= self.b, f"Random number is not in the expected range [{self.a}, {self.b}]"


class TestRandomFloatUniform:
    a = -5
    b = 5
    reps = 1000

    def test_float_arithmetics(self):
        number = rnd.RndFloat('uniform', self.a, self.b)

        for _ in range(self.reps):
            result = number + 1
            assert (
                self.a + 1 <= result <= self.b + 1
            ), f"Result {result} is not in the expected range [{self.a + 1}, {self.b + 1}]"

            result = number - 1
            assert (
                self.a - 1 <= result <= self.b - 1
            ), f"Result {result} is not in the expected range [{self.a - 1}, {self.b - 1}]"

            result = number * 2
            assert (
                2 * self.a <= result <= 2 * self.b
            ), f"Result {result} is not in the expected range [{2 * self.a}, {2 * self.b}]"

            result = number / 2
            assert (
                self.a / 2 <= result <= self.b / 2
            ), f"Result {result} is not in the expected range [{self.a / 2}, {self.b / 2}]"

    def test_float_type(self):
        number = rnd.RndFloat('uniform', self.a, self.b)
        assert isinstance(number, float), f"Expected float, got {type(number)}"

    def test_float_samplers(self):
        # test str sampler with args
        number = rnd.RndFloat('uniform', self.a, self.b)
        assert self.a <= number <= self.b, f"Random number is not in the expected range [{self.a}, {self.b}]"

        # test str sampler with kwargs
        number = rnd.RndFloat('uniform', a=self.a, b=self.b)
        assert self.a <= number <= self.b, f"Random number is not in the expected range [{self.a}, {self.b}]"

        # test callable sampler with args
        number = rnd.RndFloat(uniform, self.a, self.b)
        assert self.a <= number <= self.b, f"Random number is not in the expected range [{self.a}, {self.b}]"

        # test callable sampler with kwargs
        number = rnd.RndFloat(uniform, a=self.a, b=self.b)
        assert self.a <= number <= self.b, f"Random number is not in the expected range [{self.a}, {self.b}]"
