##### Follow me on **X (Twitter)**: [@yourQuantGuy](https://x.com/yourQuantGuy)

---

## Referral Links (Get Rebates and Benefits)

#### edgeX: [https://pro.edgex.exchange/referral/QUANT](https://pro.edgex.exchange/referral/QUANT)

Permanent VIP 1 fee rate; additional 10% fee rebate; 10% extra reward points

#### Backpack: [https://backpack.exchange/join/quant](https://backpack.exchange/join/quant)

Use my referral link to get 35% fee rebate

#### Paradex: [https://app.paradex.trade/r/quant](https://app.paradex.trade/r/quant)

Use my referral link to get 10% fee rebate and 5% points bonus

#### grvt: [https://grvt.io/exchange/sign-up?ref=QUANT](https://grvt.io/exchange/sign-up?ref=QUANT)

Get 1.3x the highest points bonus network-wide; 30% manual rebate

#### Extended: [https://app.extended.exchange/join/QUANT](https://app.extended.exchange/join/QUANT)

10% instant fee reduction; 5% points bonus

---

# Cross-Exchange Arbitrage Bot

This project is a cryptocurrency futures cross-exchange arbitrage framework, intended for sharing and educational purposes only. It should not be used directly in production environments. Please use caution when trading in real markets.

## Project Overview

This project implements a cross-exchange arbitrage trading bot that currently performs spread arbitrage primarily between **edgeX** and **Lighter** exchanges. The bot executes arbitrage trades by placing post-only limit orders (maker orders) on edgeX and executing market orders on Lighter to complete the hedge.

## Features

- 🔄 **Cross-Exchange Arbitrage**: Automatically detects and exploits price spreads between two exchanges
- 📊 **Real-time Order Book Management**: Monitors order book changes in real-time via WebSocket
- 📈 **Position Tracking**: Tracks and manages trading positions in real-time
- 🛡️ **Risk Control**: Supports maximum position limits and timeout controls
- 📝 **Data Logging**: Records trading data and statistics
- ⚡ **Async Execution**: High-performance asynchronous architecture based on asyncio

## System Requirements

- Python 3.8+
- edgeX and Lighter exchange accounts
- API keys and access permissions

## Installation

### 1. Clone Repository

```bash
git clone <repository-url>
cd cross-exchange-arbitrage
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment:

**macOS/Linux:**

```bash
source venv/bin/activate
```

**Windows:**

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Copy `env_example.txt` to `.env` and fill in your API credentials:

```bash
cp env_example.txt .env
```

Edit the `.env` file and fill in your API information:

```env
# edgeX Account Credentials (Required)
EDGEX_ACCOUNT_ID=your_account_id_here
EDGEX_STARK_PRIVATE_KEY=your_stark_private_key_here

# EdgeX API Endpoints
EDGEX_BASE_URL=https://pro.edgex.exchange
EDGEX_WS_URL=wss://quote.edgex.exchange

# Lighter Configuration (Required)
API_KEY_PRIVATE_KEY=your_api_key_private_key_here
LIGHTER_ACCOUNT_INDEX=your_account_index
LIGHTER_API_KEY_INDEX=your_api_key_index
```

## Usage

### Basic Usage

```bash
python arbitrage.py --ticker BTC --size 0.002
```

### Command Line Arguments

- `--exchange`: Exchange name (default: edgex)
- `--ticker`: Trading pair symbol (default: BTC)
- `--size`: Order size per trade (required)
- `--max-position`: Maximum position limit (required)
- `--long-threshold`: Long arbitrage trigger threshold (how much higher Lighter bid price must be than edgeX ask price to trigger long edgeX arbitrage, default: 10)
- `--short-threshold`: Short arbitrage trigger threshold (how much higher edgeX bid price must be than Lighter ask price to trigger short edgeX arbitrage, default: 10)
- `--fill-timeout`: Limit order fill timeout (seconds, default: 5)

### Usage Examples

```bash
# Trade ETH, 0.01 ETH per order, set 5 second timeout
python arbitrage.py --ticker ETH --size 0.01 --long-threshold 10 --short-threshold 10 --max-position 0.1 --fill-timeout 5

# Trade BTC, limit maximum position to 0.1 BTC
python arbitrage.py --ticker BTC --size 0.002 --long-threshold 1 --short-threshold 20 --max-position 0.1
```

## Project Structure

```
cross-exchange-arbitrage/
├── arbitrage.py              # Main program entry point
├── exchanges/                # Exchange interface implementations
│   ├── base.py              # Base exchange interface
│   ├── edgex.py             # edgeX exchange implementation
│   ├── lighter.py           # Lighter exchange implementation
│   └── lighter_custom_websocket.py  # Lighter WebSocket management
├── strategy/                 # Trading strategy modules
│   ├── edgex_arb.py         # Main arbitrage strategy
│   ├── order_book_manager.py    # Order book management
│   ├── order_manager.py     # Order management
│   ├── position_tracker.py  # Position tracking
│   ├── websocket_manager.py # WebSocket management
│   └── data_logger.py       # Data logging
├── requirements.txt         # Python dependencies
├── env_example.txt          # Environment variable example
└── README.md               # Project documentation
```

## How It Works

1. **Order Book Monitoring**: Receives real-time order book updates from both exchanges via WebSocket
2. **Spread Detection**: Calculates price spreads between the two exchanges
3. **Arbitrage Opportunity Identification**: Identifies arbitrage opportunities when spreads exceed thresholds
4. **Order Execution**:
   - Places post-only limit orders (maker orders, earning fees) on edgeX
   - Executes market orders on Lighter to complete the hedge
5. **Position Management**: Tracks positions in real-time to ensure they don't exceed maximum position limits
6. **Risk Control**: Monitors order fill status and cancels orders if they don't fill within the timeout period

## Important Notes

⚠️ **Risk Warning**:

- Arbitrage trading carries market risks. Please ensure you fully understand the trading mechanisms
- It is recommended to test in a test environment or with small amounts first
- Be aware of network latency and exchange API limits
- Regularly check positions and account balance

## Dependencies

Main dependencies include:

- `python-dotenv`: Environment variable management
- `asyncio`: Asynchronous programming support
- `requests`: HTTP requests
- `tenacity`: Retry mechanism
- `edgex-python-sdk`: Official edgeX Python SDK (forked version, supports post-only limit orders)
- `lighter-python`: Lighter exchange SDK

## License

Please see the [LICENSE](LICENSE) file for details.

## Contributing

Issues and Pull Requests are welcome!

## Contact

For questions or suggestions, please contact via Issues.
