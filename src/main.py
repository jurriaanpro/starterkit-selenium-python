import time

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--disable-dev-shm-usage')


def main():
    print("Start")
    driver = None
    try:
        driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            options=options
        )

        driver.get("https://google.com")
        time.sleep(5)
    finally:
        if driver:
            driver.close()
            driver.quit()

    print("Done")

if __name__ == "__main__":
    main()
