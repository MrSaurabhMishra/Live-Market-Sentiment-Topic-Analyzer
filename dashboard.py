import streamlit as st
import mysql.connector
import pandas as pd
import plotly.express as px
import time

st.set_page_config(page_title="Pulse Market Analyzer", layout="wide")
st.title("📈 Pulse: Real-time Market Sentiment")

def get_data():
    try:
        conn = mysql.connector.connect(
            host="localhost", 
            user="root", 
            password="Saurabh1042", 
            database="pulse_db"
        )
       
        query = "SELECT * FROM sentiment_logs ORDER BY timestamp DESC LIMIT 50"
        df = pd.read_sql(query, conn)
        conn.close()
        return df
    except Exception as e:
        st.error(f"Database Connection Error: {e}")
        return pd.DataFrame()


placeholder = st.empty()


counter = 0

while True:
    df = get_data()
    
    if not df.empty:
        with placeholder.container():
            # Metrics
            c1, c2 = st.columns(2)
            latest_sentiment = df.iloc[0]['sentiment']
            latest_topic = df.iloc[0]['topic']
            
            c1.metric("Current Market Sentiment", latest_sentiment)
            c2.info(f"**Emerging Topics (LDA):** {latest_topic}")
            
            
            fig = px.line(df, x='timestamp', y='confidence', color='ticker', 
                          title="Real-time Sentiment Pulse (Time-Series)",
                          markers=True)
            
            st.plotly_chart(fig, use_container_width=True, key=f"chart_{counter}")
            
            st.subheader("Recent Market Feeds")
            st.dataframe(df[['timestamp', 'ticker', 'sentiment', 'confidence']].head(10), use_container_width=True)
    else:
        st.warning("Waiting for data from ingestion_processor.py... Make sure it is running!")

    counter += 1
    time.sleep(1)
    
  