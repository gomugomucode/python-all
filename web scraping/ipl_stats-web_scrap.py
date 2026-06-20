import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# -----------------------
# Start Browser
# -----------------------
driver = webdriver.Chrome()

# Dictionary to store every season
all_seasons = {}

# -----------------------
# Loop through seasons
# -----------------------
for season in range(2008, 2027):

    print(f"Scraping {season}...")

    # Open season page
    driver.get(
        f"https://www.iplt20.com/stats/{season}"
    )

    # Wait until table appears
    table = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "/html/body/div[1]/div[2]/div[4]/div/section/div/div[3]/div[2]/div[2]/div/div[3]/div/div[1]/table/tbody"
            )
        )
    )

    # Get text from table
    data = table.text

    # Split into rows
    rows = data.split("\n")

    # First row contains column names
    columns = rows[0].split()

    # Remaining rows contain player data
    player_rows = rows[1:]

    # Store rows in list
    season_data = []

    for row in player_rows:
        season_data.append(row)

    # Create DataFrame
    df = pd.DataFrame(
        season_data,
        columns=["Raw_Data"]
    )

    # Store DataFrame in dictionary
    all_seasons[season] = df

    print(
        f"{season} completed"
    )

# Close browser
driver.quit()


all_seasons[2026].head()






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