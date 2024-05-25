# Real-time Stock Price Dashboard

## Introduction
This project is a real-time stock price dashboard built with FastAPI, WebSockets, and Chart.js. It fetches real-time stock data and visualizes it in a live updating chart.

## Features
- Real-time data updates using WebSockets
- Interactive line chart with Chart.js
- Backend powered by FastAPI

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/sbstnzcr/fastapi-stock-price-dashboard.git
    cd fastapi-stock-price-dashboard
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the FastAPI server:
    ```bash
    uvicorn app:app --reload
    ```

4. Open your browser and go to `http://localhost:8000`.