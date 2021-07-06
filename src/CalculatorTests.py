import unittest
from Calculator import Calculator
from CsvReader import CsvReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        calculator = Calculator();
        self.assertIsInstance(calculator, Calculator)

    def test_results_property_calculator(self):
        calculator = Calculator();
        self.assertEqual(calculator.result, 4)

    def test_add_method_calculator(self):
       test_data = CsvReader('./src/Unit Test Addition.csv').data
       for row in test_data:
        self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
        self.assertEqual(self.calculator.result, int(row['Result']))

    def test_subtract_method_calculator(self):
        test_data = CsvReader('./src/Unit Test Subtraction.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_multiply_method_calculator(self):
        test_data = CsvReader('./src/Unit Test Multiplication.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_division_method_calculator(self):
        test_data = CsvReader('./src/Unit Test Division.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.divide(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    def test_square_method_calculator(self):
        test_data = CsvReader('./src/Unit Test Square.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.sq(row['Value 1']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_square_root_method_calculator(self):
        test_data = CsvReader('./src/Unit Test Square Root.csv').data
        for row in test_data:
            self.assertAlmostEqual(self.calculator.sqrt(row['Value 1']), float(row['Result']))
            self.assertAlmostEqual(self.calculator.result, float(row['Result']))


if __name__ == '__main__':
    unittest.main()
