from fastapi import FastAPI
from enum import Enum

app = FastAPI()

items  = {
    'Indian': ["Saravanaa Bhavan", "A2B", "Thalapakatti"],
    'Mexican': ["Chipotle", "Baja Fresh"]
}

class AvailableCuisines(str, Enum):
    indian = 'indian'
    american = 'american'
    italian = 'italian'

@app.get("/")
def hello():
    return "Hello World"

@app.get("/name/{name}")
def hello(name):
    return f"Hello {name}"

coupon_code = {
    1: '10%',
    2: '20%',
    3: '30%'
}

@app.get("/get_cuisine/{cuisine}/{location}")
def get_cuisine(cuisine: AvailableCuisines, location):
    return f"{cuisine} restaurants in {location}: {items[cuisine]}"


@app.get("/get_coupon/{code}")
def get_coupons(code: int):
    return { 'discount_amount': coupon_code.get(code)}