# LinkedIn Job Scraper (Sweden)

A Python project to scrape job postings from **LinkedIn Sweden** using Selenium.  
The scraper extracts job details (title, company, location, posted date, application numbers, job requirements, description, and URL) and saves them to CSV files for further analysis.

---

## 🚀 Features
- Scrape job postings by pages (25 jobs per page).
- Extract key details:
  - Job Title  
  - Company  
  - Location  
  - Posted Time  
  - Application Numbers  
  - Job Details (translated into English)  
  - Job Description  
  - URL  
- Automatic CSV saving (supports incremental saving every 25 jobs).
- Failed jobs are logged separately for later re-scraping.
- Support for **cookie-based login** to avoid repeated manual logins.

---

## 📂 Project Structure
.
├── get_data.py # Extract job IDs, scrape job details, save results to CSV
├── log_in.py # Cookie-based LinkedIn login
├── main.py # Main script to run the scraper
├── set_up.py # Selenium WebDriver setup
├── requirements.txt # Dependencies
├── .gitignore # Files to ignore (cookies, CSV outputs, venv, etc.)
└── README.md # Project documentation

yaml
---

## ⚙️ Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/linkedin-job-scraper.git
   cd linkedin-job-scraper
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux / macOS
   venv\Scripts\activate      # Windows
3. Install dependencies:
   ```bash
   pip install -r requirements.txt

▶️ Usage
1. Prepare LinkedIn cookies

  - Log in to LinkedIn manually in your browser.
  - Export cookies (e.g., using a browser extension).
  - Save them into a file named cookies.pkl.

2. Run the scraper:
   ```bash
   python main.py

3. Output
Scraped data will be saved into CSV files:
  - linkedin_jobs_xxx.csv (job data)
  - failed_jobs.csv (failed job IDs)

📊 Example Analysis
Once you collect ~1000 job postings, you can analyze:

📍 Top hiring locations (e.g., Stockholm, Gothenburg, Malmö).

🏢 Top hiring companies in Sweden.

📈 Most demanded job titles and trends.

💡 Required skills & requirements (translated to English).

⏳ Posting trends (how long jobs stay open).

⚠️ Disclaimer
This project is for educational and research purposes only.

Scraping LinkedIn may violate their Terms of Service. Use responsibly.

The author is not responsible for any misuse of this project.

📌 License
MIT License.
Free to use and modify, but please give credit to the author.
