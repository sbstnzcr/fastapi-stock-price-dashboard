import asyncio

import aiohttp
from fastapi import FastAPI, WebSocket
from fastapi.responses import FileResponse

API_KEY = "4KP4G1NKOG8UR4M1"
STOCK_SYMBOL = "AAPL"  # Replace with the stock symbol you want to track
API_URL = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={STOCK_SYMBOL}&interval=1min&apikey={API_KEY}"

app = FastAPI()


@app.get("/")
async def root() -> FileResponse:
    return FileResponse("static/index.html")


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket) -> None:
    await websocket.accept()
    async with aiohttp.ClientSession() as session:
        while True:
            async with session.get(API_URL) as response:
                if response.status != 200:
                    await websocket.send_json({"error": "API request failed"})
                    continue
                data = await response.json()
                latest_time = sorted(data["Time Series (1min)"].keys())[0]
                latest_price = data["Time Series (1min)"][latest_time]["1. open"]
                await websocket.send_json({"time": latest_time, "price": latest_price})
            await asyncio.sleep(60)
