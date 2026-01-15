# 🛒 Amazon Price Tracker (Flask Web App)

A simple **Amazon Price Tracker** built using **Flask**, **Requests**, and **BeautifulSoup**.
This web application allows users to paste an Amazon product URL and instantly fetch the **current product price** in a clean and responsive UI.

---

## 📸 Preview

> Enter an Amazon product URL → Click **Check Price** → View the current price instantly.

---

## 🚀 Features

* 🔗 Accepts Amazon product URLs
* 💰 Scrapes and displays current product price
* ⚡ Fast and lightweight Flask backend
* 🎨 Modern UI using Bootstrap 5
* 🛡 Handles request and parsing errors gracefully

---

## 🛠 Tech Stack

* **Backend:** Python, Flask
* **Web Scraping:** Requests, BeautifulSoup (bs4)
* **Frontend:** HTML, CSS, Bootstrap 5

---

## 📂 Project Structure

```
amazon-price-tracker/
│
├── app.py
├── templates/
│   └── index.html
├── requirements.txt
└── README.md
```

---

## 📦 Requirements

Make sure you have **Python 3.8+** installed.

### Python Libraries Used

* flask
* requests
* beautifulsoup4

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```
git clone https://github.com/Doremon-tech-svg/amazon-price-tracker.git
cd amazon-price-tracker
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)

```
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```
pip install flask requests beautifulsoup4
```

Or using `requirements.txt`:

```
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```
python app.py
```

The app will start at:

```
http://127.0.0.1:5000/
```

---

## 🧠 How It Works

1. User submits an **Amazon product URL**
2. Flask sends a request with browser-like headers
3. BeautifulSoup parses the HTML page
4. Extracts:

   * `a-price-whole`
   * `a-price-fraction`
5. Combines and displays the price on the UI

---

## ⚠️ Important Notes

* Amazon frequently changes its HTML structure
* Some products may not return a price due to:

  * CAPTCHA
  * Region restrictions
  * Dynamic pricing
* This project is for **educational purposes only**

---

## 🔮 Future Improvements

* 📉 Price drop alerts via email
* ⏰ Scheduled price tracking
* 📊 Price history graph
* 🌍 Multi-country Amazon support
* 🔐 CAPTCHA & proxy handling

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork the repository and submit a pull request.

---

## 📜 Disclaimer

This project is **not affiliated with Amazon**.
Web scraping may violate Amazon’s Terms of Service.
Use responsibly and for learning purposes only.

---

## ❤️ Author

**DIVYANK**
Made with ❤️ using Python & Flask

---

## ⭐ Su
