import sys
import os

sys.path.append("..")

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from connect import Base
from models import Score
from math_functions import Math

import unittest


class MathFunctionsTest(unittest.TestCase):

    def setUp(self):
        engine = create_engine("sqlite:///scores.db")
        Base.metadata.create_all(engine)
        session = Session(bind=engine)

        self.math = Math(session, "Player1")

    def tearDown(self):
        os.remove("scores.db")

    def test_get_random_number(self):
        results = []
        for i in range(50):
            results.append(self.math.get_random_number())

        self.assertIn(2, results)

    def test_get_random_operation(self):
        results = []
        for i in range(50):
            results.append(self.math.get_random_operation())

        self.assertIn("+", results)

    def test_is_divisible_true_operation_division(self):
        self.assertTrue(self.math.is_divisible(4, 2, "/"))

    def test_is_divisible_true_operation_not_division(self):
        self.assertTrue(self.math.is_divisible(4, 2, "+"))

    def test_is_divisible_false_operation_division(self):
        self.assertFalse(self.math.is_divisible(3, 2, "/"))

    def test_result_plus(self):
        self.assertEqual(self.math.result(1, 2, "+"), "3")

    def test_result_minus(self):
        self.assertEqual(self.math.result(3, 2, "-"), "1")

    def test_result_multiply(self):
        self.assertEqual(self.math.result(3, 2, "*"), "6")

    def test_result_divide(self):
        self.assertEqual(self.math.result(6, 2, "/"), "3")

    def test_result_power(self):
        self.assertEqual(self.math.result(2, 3, "^"), "8")

    def test_make_random_expression(self):
        results = []
        for i in range(1000):
            self.math.make_random_expression()
            results.append([self.math.operation["expression"], self.math.operation["result"]])

        self.assertIn(["What is the answer to 2 + 3?", "5"], results)

    def test_get_score_has_played(self):
        score_object = Score(player="Player1", score=9)
        self.math.session.add(score_object)
        self.math.session.commit()
        self.math.score = 3
        expected_result = {"has_played": True, "player_score": 9}
        self.assertEqual(self.math.get_score(), expected_result)

    def test_get_score_has_not_played(self):
        expected_result = {"has_played": False, "player_score": 0}
        self.assertEqual(self.math.get_score(), expected_result)


if __name__ == '__main__':
    unittest.main()
