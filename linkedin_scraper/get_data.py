# @Author : Yulia
# @File   : get_data.py
# @Time   : 2025/8/6 16:43
import os
import random
import time
import pandas as pd
from deep_translator import GoogleTranslator
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def get_job_ids_on_current_page(driver, wait):
    """get all job_id on current page"""
    job_cards = wait.until(EC.presence_of_all_elements_located(
        (By.XPATH, "//*[@id='main']/div/div[2]/div[1]/div/ul/li")
    ))
    job_ids = [card.get_attribute("data-occludable-job-id") for card in job_cards if card.get_attribute("data-occludable-job-id")]
    print(f"Collected {len(job_ids)} job ids.")
    return job_ids


def scrape_job_details(driver, wait, job_id, idx, page_start, failed_jobs):
    """retry when fails"""
    def get_text_safe(locator, retries=2, delay=1):
        for _ in range(retries):
            try:
                return driver.find_element(*locator).text.strip()
            except:
                time.sleep(delay)
        return "N/A"

    # url of single job's detail page
    job_url = f"https://www.linkedin.com/jobs/search/?currentJobId={job_id}&keywords=&location=Sweden&start={page_start}"

    # try maximum five times
    for attempt in range(5):
        try:
            driver.set_page_load_timeout(30)
            print(f"🔄 Loading job {job_id} (attempt {attempt + 1})")
            driver.get(job_url)
            wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
            time.sleep(1)
            break
        except Exception as e:
            print(f"❌ Attempt {attempt + 1} failed: {e}")
            time.sleep(random.uniform(3, 6))
            if attempt == 4:
                failed_jobs.append(job_id)
                print(f"⚠️ Failed to load job {job_id} after 5 attempts.")
                return None

    try:
        # get 'title''company''location''posted_before''application_number'for each job
        title = get_text_safe((By.XPATH, "//div[contains(@class, 'job-details-jobs-unified-top-card__job-title')]"))
        company = get_text_safe((By.XPATH, "//div[contains(@class, 'job-details-jobs-unified-top-card__company-name')]"))
        location = get_text_safe((By.XPATH, "//div[contains(@class, 'job-details-jobs-unified-top-card__primary-description-container')]/div/span/span[1]"))
        posted_before = get_text_safe((By.XPATH, "//div[contains(@class, 'job-details-jobs-unified-top-card__primary-description-container')]/div/span/span[3]"))
        application_number = get_text_safe((By.XPATH, "//div[contains(@class, 'job-details-jobs-unified-top-card__primary-description-container')]/div/span/span[5]"))

        # details for each job
        try:
            job_detail_elements = wait.until(
                EC.visibility_of_all_elements_located((By.XPATH, "//div[contains(@class, 'job-details-fit-level-preferences')]"))
            )
            job_detail = "\n".join([el.text.strip() for el in job_detail_elements])
        except:
            job_detail = "N/A"

        job_detail_en = GoogleTranslator(source='auto', target='en').translate(job_detail)

        # descriptions for each page
        job_description_elements = wait.until(
            EC.visibility_of_all_elements_located((By.XPATH, "//div[contains(@id,'job-details')]"))
        )
        job_description = "\n".join([el.text.strip() for el in job_description_elements])

        return {
            "title": title,
            "company": company,
            "location": location,
            "posted_before": posted_before,
            "application_number": application_number,
            "detail": job_detail_en,
            "description": job_description,
            "url": job_url
        }

    except Exception as e:
        print(f"[{idx + 1}] Failed: {e}")
        failed_jobs.append(job_id)
        return None


def click_next_page(driver, wait):

    try:
        next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label, 'View next page')]")))
        if "disabled" in next_button.get_attribute("class"):
            print("🔚 Last page")
            return False
        else:
            next_button.click()
            time.sleep(5)
            return True
    except Exception as e:
        print(f"warning:⚠️ fail：{e}")
        return False


def save_to_csv(data, file_path="data/linkedin_jobs.csv"):
    """save data to csv, data can be appended multiple times"""
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    df = pd.DataFrame(data)
    if os.path.exists(file_path):
        df.to_csv(file_path, mode="a", index=False, header=False, encoding="utf-8")
    else:
        df.to_csv(file_path, index=False, encoding="utf-8")

    print(f"\n✅ A total of {len(df)} pieces of data were saved to {file_path}.")

# save data to csv, old data will be covered if new data has been written in
# def save_to_csv(data, file_path="linkedin_jobs.csv"):
#     def safe_join(value):
#         if isinstance(value, list):
#             return "\n".join(v.strip() for v in value)
#         return value
#     os.makedirs(os.path.dirname(file_path), exist_ok=True)
#     for row in data:
#         if "detail" in row:
#             row["detail"] = safe_join(row["detail"])
#         if "description" in row:
#             row["description"] = safe_join(row["description"])
#
#     df = pd.DataFrame(data)
#     df.to_csv(file_path, index=False, encoding="utf-8")
#     print(f"\n✅ A total of {len(df)} pieces of data were saved to {file_path}.")