from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# Set up Selenium with ChromeDriver using webdriver_manager
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run headless (without opening a browser window)
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Navigate to the Amazon search page
URL = 'https://www.amazon.com/s?k=laptop'
driver.get(URL)

# Wait for the page to load content
time.sleep(5)  # Increase if the page takes longer to load

# Find product elements
products = []
items = driver.find_elements(By.CSS_SELECTOR, 'div.s-main-slot div[data-component-type="s-search-result"]')

# Extract product details
for item in items:
    try:
        name = item.find_element(By.CSS_SELECTOR, 'h2 a span').text.strip()
        price_whole = item.find_elements(By.CSS_SELECTOR, 'span.a-price-whole')
        price_fraction = item.find_elements(By.CSS_SELECTOR, 'span.a-price-fraction')
        if price_whole and price_fraction:
            price = f"{price_whole[0].text.strip()}.{price_fraction[0].text.strip()}"
        else:
            price = None
        
        rating = item.find_elements(By.CSS_SELECTOR, 'span.a-icon-alt')
        rating = rating[0].get_attribute("innerHTML").strip() if rating else None
        
        reviews = item.find_elements(By.CSS_SELECTOR, 'span.a-size-base')
        reviews = reviews[0].text.strip() if reviews else None

        products.append({
            'Name': name,
            'Price': price,
            'Rating': rating,
            'Reviews': reviews
        })

    except Exception as e:
        print(f"Error: {e}")

# Save data to CSV
df = pd.DataFrame(products)
df.to_csv('amazon_products.csv', index=False)

# Close the driver
driver.quit()

print("Scraping completed. Data saved to 'amazon_products.csv'.")
