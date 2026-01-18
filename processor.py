import mysql.connector
import requests
import time
from datetime import datetime
from topic import extract_topics 
import random

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "Saurabh1042",
    "database": "pulse_db"
}

def setup_db():
    conn = mysql.connector.connect(
        host=DB_CONFIG['host'],
        user=DB_CONFIG['user'],
        password=DB_CONFIG['password']
    )
    cur = conn.cursor()

    cur.execute("CREATE DATABASE IF NOT EXISTS pulse_db")
    cur.execute("USE pulse_db")

    cur.execute("""
        CREATE TABLE IF NOT EXISTS sentiment_logs (
            id INT AUTO_INCREMENT PRIMARY KEY,
            timestamp DATETIME,
            ticker VARCHAR(10),
            sentiment VARCHAR(20),
            confidence FLOAT,
            topic VARCHAR(100)
        )
    """)

    conn.commit()
    return conn


def run_ingestion():
    conn = setup_db()
    cur = conn.cursor()
    print("Ingestion Started...")
    
    while True:
       
        raw_data = [
    {"ticker": "RELIANCE", "text": "Reliance industries announces major investment in green energy sector."},
    {"ticker": "TCS", "text": "TCS reports record deal wins this quarter, but margins remain under pressure."},
    {"ticker": "HDFCBANK", "text": "HDFC Bank merger synergies are starting to reflect in the latest numbers."},
    {"ticker": "INFY", "text": "Infosys shares drop after global tech slowdown concerns rise."},
    {"ticker": "ZOMATO", "text": "Zomato hits all-time high as profitability outlook improves."}
    
]
    
        
        all_texts = [d['text'] for d in raw_data]
        current_topic = extract_topics(all_texts) 
        
        for item in raw_data:
            
            res = requests.get(f"http://localhost:8000/predict?text={item['text']}").json()
            
            
            query = "INSERT INTO sentiment_logs (timestamp, ticker, sentiment, confidence, topic) VALUES (%s, %s, %s, %s, %s)"
            cur.execute(query, (datetime.now(), item['ticker'], res['sentiment'], res['confidence'], current_topic))
        
        conn.commit()
        time.sleep(5)

if __name__ == "__main__":
    run_ingestion()