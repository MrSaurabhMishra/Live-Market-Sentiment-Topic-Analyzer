📈 Pulse — Real-Time Market Sentiment Analyzer

A production-ready, real-time market sentiment analysis platform that ingests financial news, applies deep learning–based NLP, extracts market themes, and visualizes sentiment trends through an interactive dashboard.

> Built for showcasing end-to-end data engineering + ML + backend + visualization skills.

---

## 🚀 Overview

**Pulse** continuously processes stock-market news, predicts sentiment using **FinBERT**, performs **topic modeling (LDA)** to uncover emerging themes, stores structured results in **MySQL**, and presents insights in a live **Streamlit dashboard**.

This project demonstrates practical experience with:

* Real-time pipelines
* API-based ML inference
* Database-backed analytics
* Production-style project structure
* Interactive data visualization

---

## ✨ Key Features

* **🧠 Deep Learning Sentiment Analysis**
  Uses **FinBERT (HuggingFace Transformers)** to classify financial text into **Positive, Negative, Neutral** with confidence scores.

* **🧩 Topic Modeling (LDA)**
  Automatically discovers dominant themes such as *growth*, *investment*, *risk*, *energy*, etc.

* **⚡ Real-time Processing Pipeline**
  Simulated streaming ingestion pipeline that continuously processes incoming market news.

* **🗄️ Persistent Storage**
  Stores all predictions, timestamps, and metadata into **MySQL** for analysis and scalability.

* **📊 Live Interactive Dashboard**
  Built with **Streamlit + Plotly**, auto-refreshing to display real-time sentiment trends.

* **🔄 Confidence Variation Simulator**
  Includes a variant processor to simulate real-world prediction noise and fluctuations.

---

## 🛠️ Tech Stack

| Category       | Tools & Technologies               |
| -------------- | ---------------------------------- |
| Language       | Python                             |
| Backend API    | FastAPI, Uvicorn                   |
| NLP / ML       | Transformers (FinBERT), TensorFlow |
| Topic Modeling | Gensim (LDA)                       |
| Database       | MySQL                              |
| Visualization  | Streamlit, Plotly                  |

---

## 📂 Project Structure

```
pulse/
│
├── model.py        # FastAPI service hosting FinBERT model
├── processor.py    # Main ingestion engine (API calls + DB storage)
├── rprocessor.py   # Variant processor with confidence simulation
├── topic.py        # LDA topic modeling logic
├── dashboard.py    # Streamlit real-time dashboard
├── req.txt         # Project dependencies
└── README.md       # Documentation
```

---

## ⚙️ Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/pulse-sentiment-analyzer.git
cd pulse-sentiment-analyzer
```

### 2. Configure MySQL

Ensure MySQL is installed and running.

Update the `DB_CONFIG` variable inside:

* `processor.py`
* `dashboard.py`

The application will automatically create:

* Database: `pulse_db`
* Required tables on first run

---

### 3. Install Dependencies

```bash
pip install -r req.txt
```

---

### 4. Start the Sentiment API (FinBERT Server)

```bash
python model.py
```

> ⏳ First run will download the FinBERT model (~400MB)

---

### 5. Run the Ingestion Engine

Open a new terminal:

```bash
python processor.py
```

---

### 6. Launch the Dashboard

Open another terminal:

```bash
streamlit run dashboard.py
```

Now open the provided local URL in your browser to view the live dashboard.

---

## 📊 System Workflow

1. **News Ingestion**
   Simulates continuous financial news for tickers like `RELIANCE`, `TCS`, `INFY`.

2. **Sentiment Inference (FinBERT API)**
   Each news item is sent to the FastAPI endpoint for prediction.

3. **Topic Extraction (LDA)**
   Batches of news are analyzed to extract dominant themes and keywords.

4. **Database Storage**
   Results (text, sentiment, confidence, timestamp, ticker) are saved in MySQL.

5. **Live Visualization**
   Streamlit dashboard auto-refreshes to show evolving market sentiment.

---

## 📌 Use Cases

* Market sentiment tracking
* Financial news intelligence
* ML + backend portfolio project
* Real-time analytics demo
* NLP system design showcase

---

## 🔮 Future Improvements

* Real news ingestion (NewsAPI, Twitter/X, RSS feeds)
* Kafka / Redis streaming integration
* Docker containerization
* Cloud deployment (AWS / GCP)
* User authentication for dashboard
* Advanced sentiment aggregation per stock

---

## 👨‍💻 Author

**Saurabh Mishra**
AI Engineer / Data Scientist / AI/ML Developer

* GitHub: [https://github.com/your-username](https://github.com/mrsaurabhmishra)
* LinkedIn: [https://linkedin.com/in/your-profile](https://linkedin.com/in/Mrsaurabhmishra)

---

## ⭐ If you like this project

Give it a star ⭐ and feel free to fork and improve it!
_
