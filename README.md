# Automotive Market Specs Analysis: Upcoming Vehicles

An end-to-end data analytics project that programmatically extracts unstructured web data on upcoming vehicles, processes and engineers key market features using Python, and delivers an interactive data visualization dashboard via Tableau Public.

**[View the Interactive Tableau Dashboard Here](https://tabsoft.co/49yEBrp)** *(Note: Replace this placeholder text with your actual shortened Bitly or Tableau Public link!)*

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
