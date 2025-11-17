import requests
from bs4 import BeautifulSoup
import sys

TARGET_URL = "https://timesofindia.indiatimes.com/home/headlines"  # main headlines page of TOI
OUTPUT_FILE = "headlines.txt"
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; TOI-headline-scraper/1.0)"}
TIMEOUT = 10.0

def fetch_page(url):
    resp = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
    resp.raise_for_status()
    return resp.text

def extract_headlines(html):
    soup = BeautifulSoup(html, "html.parser")
    headlines = []
    seen = set()
    # Using the list items under the headlines page
    # Example structure observed: bullet list items “li” with anchor text
    for li in soup.select("li"):
        text = li.get_text(strip=True)
        if text and len(text) > 20:
            if text not in seen:
                seen.add(text)
                headlines.append(text)
    return headlines

def save_headlines(hlist, filename=OUTPUT_FILE):
    with open(filename, "w", encoding="utf-8") as f:
        for h in hlist:
            f.write(h + "\n")

def main():
    try:
        print("Fetching page:", TARGET_URL)
        html = fetch_page(TARGET_URL)
        print("Parsing headlines …")
        headlines = extract_headlines(html)
        if not headlines:
            print("No headlines found. You might need to change the selector for the site structure.")
            sys.exit(1)
        print(f"Found {len(headlines)} headlines.")
        print("Saving to file:", OUTPUT_FILE)
        save_headlines(headlines)
        print("Done.")
    except Exception as e:
        print("Error:", e)
        sys.exit(2)

if __name__ == "__main__":
    main()