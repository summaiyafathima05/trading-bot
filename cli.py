import argparse
import os
import sys
from dotenv import load_dotenv
from client import BinanceClient
from orders import place_order

load_dotenv()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--symbol', required=True)
    parser.add_argument('--side', required=True)
    parser.add_argument('--type', dest='order_type', required=True)
    parser.add_argument('--quantity', required=True, type=float)
    parser.add_argument('--price', type=float, default=None)
    args = parser.parse_args()

    api_key = os.getenv('BINANCE_API_KEY', '').strip()
    api_secret = os.getenv('BINANCE_API_SECRET', '').strip()

    if not api_key or not api_secret:
        print('Error: Add your API keys to .env file')
    sys.exit(1)

    client = BinanceClient(api_key=api_key, api_secret=api_secret)
    place_order(
    client=client,
    symbol=args.symbol,
    side=args.side,
    order_type=args.order_type,
    quantity=args.quantity,
    price=args.price
)


if __name__ == '__main__':
    main()
