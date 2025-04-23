from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

class Order(BaseModel):
    product_id: int
    quantity: int
    price: float

@app.post("/api/create_buy_order")
async def create_buy_order(order: Order):
    pass

    # Here you would typically process the order, e.g., save it to a database

@app.post("/api/create_sell_order")
async def create_sell_order(order: Order):
    pass

    # Here you would typically process the order, e.g., save it to a database

@app.get("/api/get_order_status")
async def get_order_status(order_id: int):
    # Here you would typically retrieve the order status from a database
    pass