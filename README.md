# Laptop Inventory Data Pipeline

## Overview

This project is a production grade ETL (Extract, Transform, Load) pipeline designed to automate the aggregation of laptop data from two of the largest IT product retailers in the region.

By engineering a centralized data warehouse, this system eliminates the need for manual browsing and provides a queryable interface for identifying inventory trends, spec-to-price ratios and stock availability.

---

## 🛠️ Tech Stack

| Technology | Role in Project |
|---|---|
| **Python 3.12** | Core programming and system logic |
| **Selenium** | Browser automation to handle dynamic content and security layers |
| **BeautifulSoup4** | DOM traversal and unstructured data extraction |
| **Pandas** | Data transformation, cleaning, and standardization |
| **SQLite3** | Relational data storage and management |

---

## 🏗️ Architecture & Scraping Strategy

The pipeline handles two distinct web architectures, demonstrating versatility in data extraction techniques.

| Feature | Industry Leader A (API-Driven) | Industry Leader B (DOM-Driven) |
|---|---|---|
| **Strategy** | Target hidden JSON payloads in button attributes | Direct parsing of HTML tags and text nodes |
| **Efficiency** | High-speed extraction via direct dictionary conversion | Robust parsing with error handling for messy strings |
| **Transformation** | Programmatic URL reconstruction from raw slugs | Currency cleaning and stock-status normalization |

---

## 🗄️ Project Structure (ETL Pattern)

To ensure scalability and maintainability, the project is decoupled into three distinct layers:

1. **Extract (`/extract`)**  
   Independent scrapers specialized in navigating specific site structures and capturing raw data.

2. **Transform (`/transform`)**  
   A centralized `cleaner.py` that utilizes Pandas to standardize columns, convert data types (e.g., currency to integers), and handle "Out of Stock" edge cases.

3. **Load (`/load`)**  
   A database management layer that commits cleaned DataFrames into the master SQLite warehouse (`bd_laptops.db`).

4. **Analytics (`query.py`)**  
   A post-load utility to run SQL queries or export database tables into portable `.csv` files.

---

## 🚀 How to Run

### 1. Clone and Initialize

```bash
git clone https://github.com/naham6/laptop-data-etl.git
cd laptop-data-etl
pip install -r requirements.txt
```

### 2. Execute the Pipeline

Run the main controllers to refresh the database with the latest market data:

```bash
python main_ryans.py
python main_startech.py
```

### 3. Analyze and Export

Utilize the query tool to find the most premium hardware or export the database back to a spreadsheet format for external reporting:

```bash
python query.py
```

---

This pipeline demonstrates how multi-source web data can be extracted, standardized, and centralized into a structured database for analysis and decision-making.
