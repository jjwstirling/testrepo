from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)

# Set up the Chrome driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Navigate to the webpage
    driver.get("https://iwha.gsk.com/cramsec/")

    # Wait for and select the radio button
    radio_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@type='radio' and @value='1']"))
    )
    radio_button.click()

    # Wait for and fill in the text box
    text_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='text' and @name='textBoxName']"))
    )
    text_box.send_keys("BNDWL23H21650")

    # Wait for and click the button
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@type='submit' and @value='Button 1']"))
    )
    button.click()

    # Wait for the table to appear (adjust the XPATH as needed)
    table = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//table"))
    )

    # Get the table HTML
    table_html = table.get_attribute('outerHTML')

    # Save the table HTML to a file
    with open("table.html", "w", encoding="utf-8") as f:
        f.write(table_html)

    print("Table HTML saved to table.html")

    # Optionally, you can also save the entire page source
    with open("full_page.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)

    print("Full page source saved to full_page.html")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()