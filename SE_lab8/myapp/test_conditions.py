from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Chrome options
options = Options()
options.add_argument("--no-sandbox")  # Disable sandbox mode

# Define test cases as a list of tuples (a, b, c, d)
test_cases = [
    (5, 10, 15, 10),  # Test case 1
    (10, 10, 20, 20),  # Test case 2
    (3, 7, 1, 5),      # Test case 3
    (2, 3, 2, 3)       # Test case 4
]

for i, (a_value, b_value, c_value, d_value) in enumerate(test_cases):
    print(f"Running Test Case {i + 1}: a={a_value}, b={b_value}, c={c_value}, d={d_value}")

    # Initialize the Chrome WebDriver for each test case
    driver = webdriver.Chrome(options=options)

    try:
        # Open your Django app's condition view page
        driver.get("http://127.0.0.1:8000/")  # Replace with your actual URL

        # Wait for a brief moment to ensure the page is fully loaded
        time.sleep(2)

        # Wait for the input fields to be present and interactable
        a_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "a"))  # Wait until the element is clickable
        )
        b_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "b"))
        )
        c_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "c"))
        )
        d_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "d"))
        )

        # Clear previous values and enter new test case values
        a_input.clear()
        b_input.clear()
        c_input.clear()
        d_input.clear()

        a_input.send_keys(str(a_value))
        b_input.send_keys(str(b_value))
        c_input.send_keys(str(c_value))
        d_input.send_keys(str(d_value))

        # Submit the form
        submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")
        submit_button.click()

        # Wait for the output to load
        time.sleep(2)

        # Print the output
        output = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h2[contains(text(), 'Output:')]//following-sibling::p"))
        )
        print("Output:", output.text)

    except Exception as e:
        print("An error occurred:", str(e))

    finally:
        # Close the browser after each test case
        driver.quit()

    # Wait for 10 seconds before the next test case
    time.sleep(2)
