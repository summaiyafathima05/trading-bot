# Binance Futures Testnet Trading Bot

A clean Python CLI application that places **Market** and **Limit** orders on the [Binance Futures Testnet (USDT-M)](https://testnet.binancefuture.com).

---

## Project Structure

```
trading_bot/
├── bot/
│   ├── __init__.py
│   ├── client.py          # Binance REST API wrapper
│   ├── orders.py          # Order placement logic + output formatting
│   ├── validators.py      # Input validation
│   └── logging_config.py  # Logging setup (file + console)
├── logs/                  # Auto-created; log files written here
├── cli.py                 # CLI entry point (argparse)
├── .env.example           # Copy to .env and fill in your credentials
├── requirements.txt
└── README.md
```

---

## Setup

### 1. Get Testnet API Credentials

1. Go to [https://testnet.binancefuture.com](https://testnet.binancefuture.com)
2. Sign in with GitHub
3. Under **API Key**, click **Generate** and copy your key + secret

### 2. Clone / Unzip the project

```bash
cd trading_bot
```

### 3. Create a virtual environment (recommended)

```bash
python -m venv venv
# macOS/Linux:
source venv/bin/activate
# Windows:
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure credentials

```bash
cp .env.example .env
# Open .env and paste your API key and secret
```

---

## How to Run

### Place a MARKET BUY order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

### Place a LIMIT SELL order

```bash
python cli.py --symbol ETHUSDT --side SELL --type LIMIT --quantity 0.1 --price 3000
```

### Place a MARKET SELL order

```bash
python cli.py --symbol BTCUSDT --side SELL --type MARKET --quantity 0.001
```

### Place a LIMIT BUY order

```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.01 --price 50000
```

### Help

```bash
python cli.py --help
```

---

## Output Example

```
──────────────────────────────────────────────────
  ORDER REQUEST SUMMARY
──────────────────────────────────────────────────
  Symbol     : BTCUSDT
  Side       : BUY
  Type       : MARKET
  Quantity   : 0.01
──────────────────────────────────────────────────

  ORDER RESPONSE
──────────────────────────────────────────────────
  Order ID     : 3924680123
  Status       : FILLED
  Executed Qty : 0.01
  Avg Price    : 65432.10
──────────────────────────────────────────────────
  ✅  Order placed successfully!
```

---

## Logging

Logs are written to `logs/trading_YYYYMMDD.log`. Each log entry includes a timestamp, log level, component name, and message. Console output shows INFO and above; the file captures DEBUG-level detail including full API request/response data.

---

## Assumptions

- Only USDT-M Futures testnet is targeted (`https://testnet.binancefuture.com`)
- `timeInForce` defaults to `GTC` (Good Till Cancelled) for LIMIT orders
- Quantity and price precision must match the symbol's rules on Binance (e.g., BTCUSDT allows up to 3 decimal places for quantity)
- Credentials are loaded from a `.env` file in the project root (or set as environment variables)
