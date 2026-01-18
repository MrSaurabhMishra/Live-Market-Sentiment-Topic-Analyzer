from fastapi import FastAPI
from transformers import AutoTokenizer, TFAutoModelForSequenceClassification
import tensorflow as tf
import uvicorn
import numpy as np

app = FastAPI()

# 1. Load FinBERT using the TF classes
tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert")
model = TFAutoModelForSequenceClassification.from_pretrained("ProsusAI/finbert", from_pt=True)

@app.get("/predict")
def predict_sentiment(text: str):
    inputs = tokenizer(text, return_tensors="tf", padding=True, truncation=True, max_length=512)
    
    
    outputs = model(inputs)
    
    
    prediction = tf.nn.softmax(outputs.logits, axis=-1)
    
    labels = ["Positive", "Negative", "Neutral"]
    
    
    confidences = prediction.numpy()[0]
    
    return {
        "sentiment": labels[np.argmax(confidences)],
        "confidence": float(np.max(confidences)),
        "text": text
    }

print("Model loaded and API is ready.")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)