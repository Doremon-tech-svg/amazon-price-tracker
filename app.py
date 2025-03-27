from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Function to scrape price from Amazon
def get_price(url):
    HEADERS = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")
    price_element = soup.find("span", {"class": "a-price-whole"})
    
    if price_element:
        return int(price_element.text.replace(",", "").strip())
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
