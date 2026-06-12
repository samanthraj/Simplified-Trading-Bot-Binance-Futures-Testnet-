# Binance Futures Testnet Trading Bot

A Python-based CLI application that places MARKET and LIMIT orders on Binance Futures Testnet (USDT-M). The project demonstrates API integration, input validation, structured project organization, logging, and exception handling.

## Features

* Place MARKET orders
* Place LIMIT orders
* Support BUY and SELL sides
* Command-line interface using argparse
* Input validation
* Logging to file
* Error handling for invalid inputs and API failures
* Binance Futures Testnet integration

## Project Structure

```text
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── cli.py
├── requirements.txt
├── README.md
└── .env
```

## Requirements

* Python 3.10+
* Binance Futures Testnet Account
* Binance Futures Testnet API Key and Secret

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd trading_bot
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root:

```env
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret
```

## Usage

### MARKET Order

```bash
python cli.py \
--symbol BTCUSDT \
--side BUY \
--type MARKET \
--quantity 0.001
```

### LIMIT Order

```bash
python cli.py \
--symbol BTCUSDT \
--side SELL \
--type LIMIT \
--quantity 0.001 \
--price 120000
```

## Validation

The application validates:

* Side (BUY / SELL)
* Order Type (MARKET / LIMIT)
* Quantity greater than zero
* Price required for LIMIT orders

## Logging

Application events are recorded in:

```text
trading_bot.log
```

Logged events include:

* Order requests
* Successful responses
* Validation failures
* API errors
* Unexpected exceptions

## Error Handling

The application handles:

* Invalid user input
* Missing parameters
* Binance API errors
* Network-related failures
* Unexpected exceptions

## Example Output

```text
Order Request

Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.001

Order Response

Order ID: 123456789
Status: FILLED
Executed Qty: 0.001

Order Successful
```

## Assumptions

* User has a valid Binance Futures Testnet account.
* API credentials are configured correctly.
* Orders are placed only on Binance Futures Testnet.
* Internet connectivity is available.

## Learning Outcomes

This project helped reinforce:

* Python project structure
* API integration
* CLI development using argparse
* Logging and monitoring
* Exception handling
* Input validation
* Environment variable management

```
```
