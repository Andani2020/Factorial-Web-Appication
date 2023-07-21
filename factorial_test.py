import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

# Function to calculate factorial of a number
def factorial(num):
    return math.factorial(num)

class TestFactorialCalculator(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://localhost:6464")

    def test_calculate_factorial(self):
        input_number = 7

        # Find the input element for entering the number
        input_field = self.driver.find_element(By.ID, "number")
        input_field.send_keys(str(input_number))

        # Find and click the "Calculate" button
        calculate_button = self.driver.find_element(By.ID, "getFactorial")
        calculate_button.click()

        # Wait for the result to be displayed
        self.driver.implicitly_wait(10)

        # Find the result element and extract the calculated factorial
        result_element = self.driver.find_element(By.ID, 'resultDiv')
        factorial_result = result_element.text

        # Split the string at the colon ":" and take the last part
        number_part = factorial_result.split(":")[-1]

        # Remove any whitespaces and convert to an integer
        result_number = int(number_part.strip())

        # Calculate the factorial of 7 using the factorial function
        expected_result = factorial(input_number)

        # Assert that the calculated factorial matches the expected result
        self.assertEqual(result_number, expected_result, f"Factorial of {input_number} is incorrect. Expected: {expected_result}, Actual: {result_number}")

        print(f"Factorial of {input_number} is calculated correctly: {input_number}! = {result_number}")

    def tearDown(self):
        # Close the browser window
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
