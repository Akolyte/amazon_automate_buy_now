import requests
from bs4 import BeautifulSoup
import time
import random
import webbrowser
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# --- CONFIG ---
JOB_TITLE = "Machine Learning Engineer"
NUMBER_OF_SECONDS_TO_WAIT = 600
LOCATION_ID = "90000070"  # Location ID for "United States"
SALARY = 120000

def main():
    logging.info("Starting job automation script...")
    logging.info(f"Job Title: {JOB_TITLE}")
    logging.info(f"Location ID: {LOCATION_ID}")
    logging.info(f"Salary: {SALARY}")
    logging.info(f"Waiting time: {NUMBER_OF_SECONDS_TO_WAIT} seconds")

    # Start the job automation process
    job_automation()

def job_automation():
    while True:
        try:
            if is_jobs_available():
                open_in_chrome()
                logging.info("Job available! Opening in Chrome.")
            else:
                logging.info("No jobs available. Waiting for next check.")
        except Exception as e:
            logging.error(f"Error: {e}")

        sleep_time = random.randint(SLEEP_MIN, SLEEP_MAX)
        logging.info(f"Waiting {sleep_time} seconds before next check...")
        time.sleep(sleep_time)

def is_jobs_available():
    response = requests.get(LINKEDIN_URL, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept-Language": "en-US,en;q=0.9",})
    soup = BeautifulSoup(response.text, 'html.parser')
    # Soup Debugging
    #with open("soup_contents.txt", "w", encoding="utf-8") as f:
        #f.write(soup.prettify())

    no_jobs_banner = soup.find('strong', class_='no-results__main-title-keywords')
    if no_jobs_banner:
        return False
    return True

def open_in_chrome():
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(LINKEDIN_URL)

def encode_spaces(text):
    return text.replace(' ', '%20')

SLEEP_MIN = NUMBER_OF_SECONDS_TO_WAIT - 50
SLEEP_MAX = NUMBER_OF_SECONDS_TO_WAIT + 50
SALARY_LEVELS = {
    40000: 1,
    60000: 2,
    80000: 3,
    100000: 4,
    120000: 5,
    140000: 6,
    160000: 7,
    180000: 8,
    200000: 9,
}
LINKEDIN_URL = f"https://www.linkedin.com/jobs/search/?currentJobId=4180906838&f_SB2={SALARY_LEVELS[SALARY]}&f_TPR=r{NUMBER_OF_SECONDS_TO_WAIT}&geoId={LOCATION_ID}&keywords={encode_spaces(JOB_TITLE)}&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=R"

if __name__ == "__main__":
    main()
