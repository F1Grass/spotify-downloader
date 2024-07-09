from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up the WebDriver with headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

try:
    # Open the website
    driver.get("https://spowload.com/")

    # Find the input field for the Spotify link
    input_field = driver.find_element(By.NAME, "spotify_url")  # Adjust this based on the actual name attribute of the input field

    # Paste the Spotify link (you can replace this with any Spotify link you want)
    spotify_link = "https://open.spotify.com/track/4cOdK2wGLETKBW3PvgPWqT?si=123456"
    input_field.send_keys(spotify_link)

    # Submit the form (assuming there's a form to submit)
    input_field.send_keys(Keys.RETURN)

    # Wait for the conversion to complete and the download button to appear
    time.sleep(10)  # Adjust this time based on the actual time it takes for the site to convert and display the download button

    # Find the download button and click it
    download_button = driver.find_element(By.XPATH, "//a[@class='btn btn-success']")  # Adjust the XPath based on the actual button's properties
    download_button.click()

    # Wait for the download to start (you might need to adjust this based on your browser's behavior)
    time.sleep(10)  # Adjust this time based on the download initiation

finally:
    # Close the WebDriver
    driver.quit()

