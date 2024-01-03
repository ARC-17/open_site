from selenium import webdriver
import time

def load_page(url):
    try:
        driver = webdriver.Chrome()

        driver.get(url)
        print(f"Page loaded successfully at {time.ctime()}")

    except Exception as e:
        print(f"Error loading page: {e}")

    finally:
        driver.quit()

if __name__ == "__main__":
    url = "https://github.com/ARC-17"

    # Time interval in seconds
    time_interval = 20 

    try:
        while True:
            load_page(url)
            time.sleep(time_interval)

    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
