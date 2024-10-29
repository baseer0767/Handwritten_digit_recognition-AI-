from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()

options.add_argument("--no-sandbox")  # Disable sandbox mode

options.add_argument("--disable-usb-discovery--")

driver = webdriver.Chrome(options=options)

driver.get(" http://www.youtube.com/")

# Print the title of the page
print("Page title is:", driver.title)

    # Pause the script
input("Press Enter to close the browser...")