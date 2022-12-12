import unittest
import src.calculator as calc 

class TestCalculator(unittest.TestCase):
    def test_sum_numbers_returns_sum_of_integers(self):
        result = calc.sum(2, 3)
        self.assertEqual(result, 5)

    def test_sum_numbers_works_with_negative_numbers(self):
            result = calc.sum(-2, -3)
            self.assertEqual(result, -5)

    def test_sum_numbers_returns_sum_of_floats(self):
            result = calc.sum(2.4, 3.2)
            self.assertEqual(result, 5.6)

    def test_sum_numbers_returns_sum_of_integer_and_float(self):
            result = calc.sum(2, 3.2)
            self.assertEqual(result, 5.2)

    def test_sum_numbers_takes_rises_error_if_parameters_are_not_numbers(self):
            with self.assertRaises(TypeError):
                calc.sum(1, "a")

#Test subtraction 

    def test_subtraction_numbers_returns_difference_of_integers(self):
        result = calc.subtraction(3, 2)
        self.assertEqual(result, 1)

    def test_subtraction_numbers_works_with_negative_numbers(self):
            result = calc.subtraction(-2, -3)
            self.assertEqual(result, 1)

    def test_subtraction_numbers_returns_sum_of_floats(self):
            result = calc.subtraction(3.2, 2.4)
            self.assertEqual(result, 0.8)

    def test_subtraction_numbers_returns_sum_of_integer_and_float(self):
            result = calc.subtraction(2, 3.2)
            self.assertEqual(result, -1.2)

    def test_subtraction_numbers_takes_rises_error_if_parameters_are_not_numbers(self):
            with self.assertRaises(TypeError):
                calc.subtraction(1, "a")

#Test multiplication

    def test_multip_numbers_returns_product_of_integers(self):
        result = calc.multip(3, 2)
        self.assertEqual(result, 6)

    def test_multip_numbers_works_with_negative_numbers(self):
            result = calc.multip(-2, -3)
            self.assertEqual(result, 6)

    def test_multip_numbers_returns_prod_of_floats(self):
            result = calc.multip(3.2, 2.4)
            self.assertEqual(result, 7.68)

    def test_multip_numbers_returns_sum_of_integer_and_float(self):
            result = calc.multip(2, 3.2)
            self.assertEqual(result, 6.4)

    def test_multip_numbers_takes_rises_error_if_parameters_are_not_numbers(self):
            with self.assertRaises(TypeError):
                calc.multip(1, "a")

if __name__ == '__main__':

    unittest.main()