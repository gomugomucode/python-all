# Worldometers COVID-19 Web Scraper

A Python web scraping project that fetches real-time COVID-19 statistics from [Worldometers](https://www.worldometers.info/coronavirus/) using `requests` and `BeautifulSoup`, parses the main data table, converts the results into a Pandas DataFrame, and exports the data to a CSV file.

---

## 📁 Project Structure

```text
web scraping/
├── main.py                         # Main Python script for scraping and saving data
├── world_ometers_corona_data.csv   # Output CSV file containing scraped data
└── README.md                       # Project documentation
```

---

## 🛠️ Required Dependencies

This project requires Python 3.x and the following third-party libraries:

- **`requests`**: For fetching web pages over HTTP.
- **`beautifulsoup4` (`bs4`)**: For parsing HTML document trees.
- **`pandas`**: For tabular data manipulation and saving output to CSV format.

---

## 🚀 Setup & Execution

### 1. Activate Virtual Environment

Ensure your virtual environment is active. In PowerShell:
```powershell
.\.venv\Scripts\activate
```

### 2. Install Required Packages

If dependencies are missing, install them using:
```bash
pip install requests beautifulsoup4 pandas
```

### 3. Run the Web Scraper

Execute the script:
```bash
python main.py
```

---

## 📋 How It Works

1. **HTTP Request**: Sends a `GET` request to `https://www.worldometers.info/coronavirus/`.
2. **HTML Parsing**: Parses the response content using `BeautifulSoup(response.content, "html.parser")`.
3. **Table Extraction**: Finds the table element with `id="main_table_countries_today"`.
4. **Header Extraction**: Loops through `<th>` tags to extract table column headers.
5. **Row Data Extraction**: Iterates over `<tr>` rows and extracts text contents from `<td>` tags, performing string stripping (`.strip()`).
6. **Data Structuring & Export**: Constructs a Pandas `DataFrame` and saves the result to `world_ometers_corona_data.csv`.
