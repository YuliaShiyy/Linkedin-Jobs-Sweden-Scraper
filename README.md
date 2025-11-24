markdown
# LinkedIn Job Scraper (Sweden)

A Python-based scraper for collecting LinkedIn Sweden job postings using Selenium.
The tool extracts structured job information, enriches the text with LLM-powered parsing, and exports cleaned datasets for downstream analytics such as market trend analysis, skill extraction, and hiring insights.

---

## 🚀 Features
🔍 Core Scraping
- Paginated scraping (25 jobs per page)
- Extracts:
  -Job Title
  -Company
  -Location
  -Posted Time
  -Number of Applicants
  -Job Requirements / Key Details
  -Full Job Description
  -Job URL

🤖 LLM-Assisted Enrichment (Optional / Pluggable)

-Title normalization

-Job category classification

-Skill extraction from unstructured descriptions

-Text cleanup & translation support

-Modular design (llm_enrichment.py) allows:

  -Real LLM API (OpenAI/DeepSeek/etc.)

  -Or rule-based mock enrichment (cost-free)

💾 Data Handling

-Auto-saving after every page (25 rows)

-Failed job IDs stored separately for later re-run

-Output stored with timestamped filenames

-Fault-tolerant scrapers with retries & safe extraction

🔐 Authentication

Cookie-based login (no repeated manual login)

---

## 📂 Project Structure
    .
    ├── data
    │   └── linkedin_jobs_250809_final # store the final results, which contains 1000 rows
    ├── linkedin_scraper
    │   ├── get_data.py # Extract job IDs, scrape job details, save results to CSV
    │   ├── log_in.py # Cookie-based LinkedIn login
    │   ├── main.py # Main script to run the scraper
    │   └── set_up.py # Selenium WebDriver setup
    ├── output
    │   └── linkedin_jobs_20250810_003215_final.csv # store sample results, which contains 175 rows
    ├── .gitignore # Files to ignore (cookies, CSV outputs, venv, etc.)
    ├── README.md # Project documentation
    └── requirements.txt # Dependencies

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
