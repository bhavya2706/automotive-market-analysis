# Automotive Market Specs Analysis: Upcoming Vehicles

An end-to-end data analytics project that programmatically extracts unstructured web data on upcoming vehicles, processes and engineers key market features using Python, and delivers an interactive data visualization dashboard via Tableau Public.

**[View the Interactive Tableau Dashboard Here](https://public.tableau.com/)** *(Note: Replace this placeholder text with your actual shortened Bitly or Tableau Public link!)*

---

## 📌 Project Architecture

The project follows a structured, modular data pipeline to separate data collection from transformation, minimizing server load and optimizing code maintainability.

```text
[CarWale Website] 
       │
       ▼ (BeautifulSoup / requests)
[scraped_vehicles.csv] (Raw Data)
       │
       ▼ (Pandas / Regular Expressions)
[dashboard_ready_vehicles.csv] (Cleaned & Engineered)
       │
       ▼ (Data Connection)
[Tableau Public Dashboard] (Interactive BI Presentation)
```

---

## 🛠️ Tech Stack & Libraries

* **Data Extraction:** `Python 3.13`, `BeautifulSoup4`, `Requests`
* **Data Processing & Feature Engineering:** `Pandas`, `Regular Expressions (re)`
* **Business Intelligence & Visualization:** `Tableau Public`
* **Version Control:** `Git` / `GitHub`

---

## 📂 Repository Structure

```text
├── carwale_scraper.py           # Script 1: Programmatic web scraper targeting parent containers
├── data_cleaning.py             # Script 2: Data preprocessing, regex parsing, and market segmentation
├── scraped_vehicles.csv         # Extracted raw text data from the web pipeline
└── dashboard_ready_vehicles.csv # Final curated dataset optimized for BI tools
```

---

## ⚙️ Core Pipeline Implementation

### 1. Web Scraping (`carwale_scraper.py`)
Extracts structural HTML cards, isolating relevant document object fragments containing vehicle names, estimated prices, and launching information. It addresses request overhead and utilizes local formatting standards.

### 2. Data Preprocessing & Feature Engineering (`data_cleaning.py`)
A standalone post-processing script built to clean, compute, and group unstructured text.

* **Regex Numeric Conversion:** Parses complex hyphenated pricing structures (e.g., `Rs. 40.00 - 50.00 Lakh`) by safely filtering out extraneous strings and currency characters, extracting decimal integers, and converting them via a structural unit multiplier mapping system into pure numerical INR values.
* **Brand Isolate Extraction:** Isolates the root manufacturer from string literals to establish corporate benchmarking categorical groups.
* **Market Price Segmentation:** Applies bin-edge definitions via `pd.cut()` to automatically group incoming models into logical market segments:
  * Budget (Under 10L)
  * Mid-Range (10L-20L)
  * Premium (20L-40L)
  * Luxury (40L+)

---

## 📊 Key Analytical Insights

Based on the visualization assets constructed on Tableau Public:

* **Market Focus:** Aggregated tracking shows an intense density of upcoming vehicle entries focused within the **Mid-Range (10L-20L)** and **Premium (20L-40L)** categories, revealing where automotive manufacturers are positioning their core volume drivers.
* **Competitive Entry Pricing:** Core baseline visual comparisons reveal distinct entry-point variances between legacy brands expanding their portfolios and high-end manufacturers targeting luxury segments.

---

## 🚀 Installation & Local Execution

To run this pipeline locally on your machine, follow these steps:

1. Clone this repository:
```bash
   git clone [https://github.com/bhavya2706/automotive-market-analysis.git](https://github.com/bhavya2706/automotive-market-analysis.git)
   cd automotive-market-analysis
   ```

2. Install the necessary data dependencies:
```bash
   pip install requests beautifulsoup4 pandas
   ```

3. Run the web scraping module to fetch raw data:
```bash
   python3 carwale_scraper.py
   ```

4. Execute the feature engineering engine to clean and prepare your dashboard file:
```bash
   python3 data_cleaning.py
   ```
