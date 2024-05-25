import asyncio

import aiohttp
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

API_KEY = "4KP4G1NKOG8UR4M1"
STOCK_SYMBOL = "AAPL"  # Replace with the stock symbol you want to track


@app.get("/", response_class=HTMLResponse)
async def get():
    with open("static/index.html", "r") as file:
        return file.read()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    async with aiohttp.ClientSession() as session:
        while True:
            url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={STOCK_SYMBOL}&interval=1min&apikey={API_KEY}"
            async with session.get(url) as response:
                data = await response.json()
                latest_time = sorted(data["Time Series (1min)"].keys())[0]
                latest_price = data["Time Series (1min)"][latest_time]["1. open"]
                await websocket.send_json({"time": latest_time, "price": latest_price})
            await asyncio.sleep(60)
