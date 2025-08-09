# @Author : Yulia
# @File   : main.py
# @Time   : 2025/8/7 20:39

import time
import os
from datetime import datetime

from log_in import log_in_with_cookies
from set_up import create_driver
from get_data import (
    get_job_ids_on_current_page,
    scrape_job_details,
    click_next_page,
    save_to_csv,
)

# ---------------- parameters ----------------
COOKIE_FILE = "cookies.pkl"  # 请在本地准备好，不要上传到GitHub
START_PAGE = 0       # start page : page 1 -> start_page = 0; page 2 -> start_page = 25; page 3 -> start_page = 50
PAGE_SIZE = 25       # job numbers per page
PAGE_TOTAL = 40    # end page of data you want to scrap
OUTPUT_DIR = "output"  # directory to save output
os.makedirs(OUTPUT_DIR, exist_ok=True)

# automatically generate filename with timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
FINAL_CSV = os.path.join(OUTPUT_DIR, f"linkedin_jobs_{timestamp}_final.csv")
FAILED_CSV = os.path.join(OUTPUT_DIR, f"linkedin_jobs_{timestamp}_failed.csv")


def main():
    driver, wait = create_driver()

    # log in with local cookies file
    log_in_with_cookies(driver)

    page_start = START_PAGE
    all_data = []
    failed_jobs = []

    driver.get(f"https://www.linkedin.com/jobs/search/?keywords=&location=Sweden&start={page_start}")
    time.sleep(3)

    while page_start < PAGE_TOTAL * PAGE_SIZE:
        print(f"🔄 Scraping page start={page_start}")
        job_ids = get_job_ids_on_current_page(driver, wait)

        for idx, job_id in enumerate(job_ids):
            data = scrape_job_details(driver, wait, job_id, idx, page_start, failed_jobs)
            if data:
                all_data.append(data)
                time.sleep(2)
            else:
                print(f"⛔ Skip job {job_id}")

            # save data after each page
            if len(all_data) % PAGE_SIZE == 0:
                save_to_csv(all_data, FINAL_CSV)

        if not click_next_page(driver, wait):
            break

        page_start += PAGE_SIZE
        time.sleep(1)

    # final file
    save_to_csv(all_data, FINAL_CSV)
    # fail file
    if failed_jobs:
        save_to_csv([{"job_id": jid} for jid in failed_jobs], FAILED_CSV)
        print(f"⚠️ There were {len(failed_jobs)} data retrieval failures, which have been saved to {FAILED_CSV}.")

    print("✅ Scraping complete!")
    driver.quit()


if __name__ == "__main__":
    main()
