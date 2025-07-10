from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Function to scrape price from Amazon
def get_price(url):
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/91.0.4472.124 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9"
    }

    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
    except requests.RequestException:
        return None  # If there's any issue with the request

    soup = BeautifulSoup(response.content, "html.parser")
    price_whole = soup.find("span", {"class": "a-price-whole"})
    price_fraction = soup.find("span", {"class": "a-price-fraction"})

    if price_whole:
        try:
            # Combine whole and fraction if both exist
            whole = price_whole.text.replace(",", "").strip()
            fraction = price_fraction.text.strip() if price_fraction else "00"
            price = float(f"{whole}.{fraction}")
            return price
        except ValueError:
            return None

    return None

# Homepage Route
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"]
        price = get_price(url)
        return render_template("index.html", price=price, url=url)
    return render_template("index.html", price=None)

if __name__ == "__main__":
    app.run(debug=True)
