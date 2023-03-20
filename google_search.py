from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# automate google search
def google_search(keyword, num_items):
    # get chrome diver
    s=Service(ChromeDriverManager().install())
    # initialize driver
    driver = webdriver.Chrome(service=s)
    # maximize window
    driver.maximize_window()
    # open google
    driver.get("https://www.google.com")

    # find input field
    search = driver.find_element(By.NAME, "q")
    # enter search keyword
    search.send_keys(keyword)
    # hit return to start seasrch
    search.send_keys(Keys.RETURN)

    # final item list
    final_items = []

    while len(final_items) < num_items:
        if (len(final_items) > 0):
            # sleep for 5 seconds in order to prevent from being banned by Google
            time.sleep(5) 
            # locate next page button
            nextBtn = driver.find_element(By.ID, "pnnext")
            # click next page button
            nextBtn.click()

        # get the list of html elements that wrap the titles and links of the search results
        links = driver.find_elements(By.CLASS_NAME, "yuRUbf")

        for link in links:
            # get the search result title
            title = link.find_element(By.CSS_SELECTOR, "h3.LC20lb")

            if title:
                url = link.find_element(By.TAG_NAME, "a").get_attribute("href")
                final_items.append([title.text, url])

                # stop searching and appending new link to the final item list
                # when the number of items is fulfilled
                if (len(final_items) == num_items):
                    break

    driver.quit()

    # print final results
    print(f"The first {len(final_items)} search results for the keyword '{keyword}':")
    for idx, item in enumerate(final_items):
        print(idx + 1, ": ", item[0], "(", item[1], ")")

# main method
def main():
    google_search("Python", 10)

if __name__ == "__main__":
    main()