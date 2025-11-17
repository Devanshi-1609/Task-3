📌 TOI Headlines Scraper

A simple Python script that scrapes the latest top headlines from The Times of India (TOI) using requests and BeautifulSoup, and saves them into a text file.

🚀 Features

        Scrapes real-time headlines from TOI Headlines page
        Uses clean HTML parsing with BeautifulSoup
        Automatically removes duplicates
        Saves headlines to headlines.txt in the project folder
        Prints the absolute file path for easy access
        Verifies content by displaying first few headlines in the terminal

🛠️ Tech Stack

        Python 3
        requests
        beautifulsoup4
        Install dependencies (if not installed):
        pip install requests beautifulsoup4

📥 How to Run

        1. Clone/download the project folder
        Open the directory in VS Code / Terminal

Run:

        python scrape_toi_headlines.py

        After execution, your headlines will be saved in:
        headlines.txt
        The script also prints the first few headlines directly in the terminal.

📄 Output File Structure (headlines.txt)

Each headline is written on a new line.

🧠 How It Works

        Script sends a GET request to the TOI Headlines page
        Parses article <a> tags containing "articleshow" (TOI’s article format)
        Extracts and cleans the text
        Removes duplicates
        Saves all valid headlines to headlines.txt

📌 File Structure

    │── scrape_toi_headlines.py
    │── headlines.txt  (auto-generated)
    │── README.md

⚠️ Notes

   - TOI site structure may change; selectors must be updated accordingly
   - Always respect website robots.txt and usage policies
   - This script is for educational purposes