# ==========================================
# IPL Stats Web Scraper (2008 - 2026)
# Beginner Friendly Version
# ==========================================

# Data manipulation
import pandas as pd

# Browser automation
from selenium import webdriver

# Used to locate elements
from selenium.webdriver.common.by import By

# Wait until elements appear
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Used for delays
import time


# ==========================================
# Start Chrome Browser
# ==========================================

driver = webdriver.Chrome()

# Dictionary to store all seasons
# Example:
# {
#     2008 : dataframe,
#     2009 : dataframe,
#     ...
# }
all_seasons = {}

# ==========================================
# Loop Through IPL Seasons
# ==========================================

for season in range(2008, 2027):

    try:

        print("=" * 50)
        print(f"Scraping IPL Season {season}")
        print("=" * 50)

        # ----------------------------------
        # Open Season Page
        # ----------------------------------

        url = f"https://www.iplt20.com/stats/{season}"

        driver.get(url)

        # Allow page to load
        time.sleep(3)

        # ----------------------------------
        # Scroll To Bottom
        # ----------------------------------
        # Some websites load content while scrolling

        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )

        time.sleep(2)

        # ----------------------------------
        # Locate Table
        # ----------------------------------

        table = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div[1]/div[2]/div[4]/div/section/div/div[3]/div[2]/div[2]/div/div[3]/div/div[1]/table/tbody"
                )
            )
        )

        # ----------------------------------
        # Extract Table Text
        # ----------------------------------

        data = table.text

        # ----------------------------------
        # Split Into Rows
        # ----------------------------------

        rows = data.split("\n")

        # First row usually contains headers
        columns = rows[0].split()

        # Actual player records
        player_rows = rows[1:]

        # ----------------------------------
        # Create DataFrame
        # ----------------------------------

        season_data = []

        for row in player_rows:
            season_data.append(row)

        df = pd.DataFrame(
            season_data,
            columns=["Raw_Data"]
        )

        # ----------------------------------
        # Store In Dictionary
        # ----------------------------------

        all_seasons[season] = df

        print(
            f"✅ {season} completed"
        )

        print(
            f"Players collected: {len(df)}"
        )

        # Small delay before next season
        time.sleep(2)

    except Exception as e:

        print(
            f"❌ Failed on season {season}"
        )

        print(e)

        # Continue to next season
        continue


# ==========================================
# Close Browser
# ==========================================

driver.quit()

# ==========================================
# Example Usage
# ==========================================

print("\nAvailable Seasons:")

print(all_seasons.keys())

print("\n2026 Data Preview:")

print(all_seasons[2026].head())

# ==========================================
# Save All Data To Excel
# ==========================================

with pd.ExcelWriter(
    "ipl_all_seasons.xlsx"
) as writer:

    for season, df in all_seasons.items():

        df.to_excel(
            writer,
            sheet_name=str(season),
            index=False
        )

print("\nExcel file saved successfully!")




# 1. Open browser
        # ↓
# 2. Open webpage
#         ↓
# 3. Locate table
#         ↓
# 4. Extract text
#         ↓
# 5. Clean data
#         ↓
# 6. Convert to DataFrame
#         ↓
# 7. Store in Dictionary
#         ↓
# 8. Save CSV/Excel