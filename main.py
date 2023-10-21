from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import csv

def search_jobs(keyword, location):
    driver = webdriver.Chrome()
    driver.get("https://indeed.com")
    time.sleep(1)

    # Fill in the location
    location_input = driver.find_element(By.ID, "text-input-where")
    ActionChains(driver).click(location_input).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).send_keys(location).perform()
    time.sleep(2)

    # Fill in the job keyword/title
    job_input = driver.find_element(By.ID, "text-input-what")
    ActionChains(driver).click(job_input).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).send_keys(keyword).perform()
    time.sleep(2)

    # Click search button
    job_input.send_keys(Keys.RETURN)
    time.sleep(5)

    csv_filename = 'jobs.csv'
    # Create or overwrite the CSV and add headers
    with open(csv_filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Title", "Company", "Location", "Salary", "Link"])

    all_jobs = []
    total_collected = 0
    page = 1
    while True:
        try:
            # Wait until the jobs list is loaded
            WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "h2.jobTitle"))
            )
            
            # Extract jobs from the current page
            job_cards = driver.find_elements(By.CSS_SELECTOR, ".jobCard_mainContent")
            for card in job_cards:
                title = card.find_element(By.CSS_SELECTOR, "h2.jobTitle span").text
                company = card.find_element(By.CSS_SELECTOR, "span.companyName").text
                job_location = card.find_element(By.CSS_SELECTOR, "div.companyLocation").text
                job_link = card.find_element(By.CSS_SELECTOR, "a").get_attribute('href')
                try:
                    salary = card.find_element(By.CSS_SELECTOR, 'div[data-testid="attribute_snippet_testid"]').text
                    if "$" not in salary:
                        continue
                except NoSuchElementException:
                    continue
                all_jobs.append([title, company, job_location, salary, job_link])
            
            # Save to CSV
            with open(csv_filename, 'a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerows(all_jobs)
                total_collected += len(all_jobs)
                print(f"Page {page} processed. Total jobs collected so far: {total_collected}.")
                all_jobs.clear()

            page += 1

            # After every 10 pages, ask user for input
            if page % 10 == 1 and page != 1:
                choice = input("Processed 10 pages. Would you like to continue? (yes/no): ")
                if choice.lower() != 'yes':
                    break

            next_page_elem = driver.find_element(By.CSS_SELECTOR, f'a[data-testid="pagination-page-{page}"]')
            next_page_elem.click()
            time.sleep(5)

        except NoSuchElementException:
            print("No more pages or job cards found.")
            break

    print(f"Saved data to {csv_filename}")
    driver.quit()
    return all_jobs

if __name__ == '__main__':
    keyword = input("Enter the job title (e.g., 'software engineer'): ")
    location = input("Enter the location (leave blank for remote jobs): ")
    search_jobs(keyword, location)
