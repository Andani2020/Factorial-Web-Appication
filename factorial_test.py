from selenium import webdriver
import math
from selenium.webdriver.common.by import By

# Function to calculate factorial of a number
def factorial(num):
    return math.factorial(num)

try:
    # Start a new instance of Chrome web browser
    driver = webdriver.Chrome()

    # Navigate to a website for factorial appliaction
    driver.get("http://localhost:6464")

    # Find the input element for entering the number
    input_field = driver.find_element(By.ID,"number")

    # Enter the number 7 to calculate the factorial of 7
    input_field.send_keys("7")

    # Find and click the "Calculate" button
    calculate_button = driver.find_element(By.ID,"getFactorial")
    calculate_button.click()

    # Wait for the result to be displayed
    driver.implicitly_wait(30)

    # Find the result element and extract the calculated factorial
    result_element = driver.find_element(By.ID,'resultDiv')
   
  
    # extract the reults from the result element
  
    factorial_result = result_element.text
    
    # Split the string at the colon ":" and take the last part
    number_part = factorial_result.split(":")[-1]

    # Remove any whitespaces and convert to an integer
    result_number = int(number_part.strip())
    
    print("The calculated results is:",result_number)
  
  
    # Calculate the factorial of 7 using fatorial function
    expected_result = factorial(7)

    # Assert that the calculated factorial matches the expected result
    assert result_number == expected_result, f"Factorial of 7 is incorrect. Expected: {expected_result}, Actual: {result_number}"

    print("Factorial of 7 is calculated correctly: 7! =", result_number)

except Exception as e:
    print("Error:", e)
    

finally:
    # Close the browser window
    driver.quit()
