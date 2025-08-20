# LinkedIn Job Scraper (Sweden)

A Python + Selenium project for scraping job postings from LinkedIn (Sweden region).  
It supports automatic login with cookies, pagination, retry handling, partial saving, and exporting results to CSV.

---

## ✨ Features
- Auto login to LinkedIn (via saved cookies)
- Scrape job postings across multiple pages
- Extract job details: title, company, location, posting time, applicants, requirements, description, and URL
- Translate job requirements into English
- Failed jobs are recorded for re-scraping later
- Results saved as timestamped CSV files

---

## 📦 Installation
Make sure you are using **Python 3.9+**.
Dependencies include: selenium，pandas， deep-translator
Install dependencies:
```bash
pip install -r requirements.txt
