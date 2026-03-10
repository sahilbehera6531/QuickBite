from fastapi import FastAPI
from pydantic import BaseModel
from textblob import TextBlob

app = FastAPI()


class FoodOrder(BaseModel):

    name: str
    quantity: int

class Review(BaseModel):

    text: str


@app.get("/")
def home():

    return {"message": "FastAPI Food Service Running"}


@app.post("/order")
def create_order(order: FoodOrder):

    return {
        "message": "Order received",
        "food": order.name,
        "quantity": order.quantity
    }

@app.post("/predict-sentiment")
def predict_sentiment(review: Review):

    analysis = TextBlob(review.text)

    polarity = analysis.sentiment.polarity

    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return {
        "review": review.text,
        "sentiment": sentiment
    }