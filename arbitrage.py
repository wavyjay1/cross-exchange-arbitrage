import asyncio
import sys
import argparse
from decimal import Decimal
import dotenv

from strategy.edgex_arb import EdgexArb


def validate_exchange(value):
    """Validate that the exchange is supported."""
    supported = ['edgex']
    if value.lower() not in supported:
        raise argparse.ArgumentTypeError(
            f"Unsupported exchange '{value}'. Supported: {', '.join(supported)}"
        )
    return value.lower()


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description='Cross-Exchange Arbitrage Bot Entry Point',
        formatter_class=argparse.RawDescriptionHelpFormatter
        )

    parser.add_argument('--exchange', type=validate_exchange, default='edgex',
                        help='Exchange to use (edgex)')
    parser.add_argument('--ticker', type=str, default='BTC',
                        help='Ticker symbol (default: BTC)')
    parser.add_argument('--size', type=str, required=True,
                        help='Number of tokens to buy/sell per order')
    parser.add_argument('--fill-timeout', type=int, default=5,
                        help='Timeout in seconds for maker order fills (default: 5)')
    parser.add_argument('--max-position', type=Decimal, default=Decimal('0'),
                        help='Maximum position to hold (default: 0)')
    parser.add_argument('--long-threshold', type=Decimal, default=Decimal('10'),
                        help='Long threshold for edgeX (default: 10)')
    parser.add_argument('--short-threshold', type=Decimal, default=Decimal('10'),
                        help='Short threshold for edgeX (default: 10)')
    return parser.parse_args()


async def main():
    """Main entry point that creates and runs the cross-exchange arbitrage bot."""
    args = parse_arguments()

    dotenv.load_dotenv()

    try:
        bot = EdgexArb(
            ticker=args.ticker.upper(),
            order_quantity=Decimal(args.size),
            fill_timeout=args.fill_timeout,
            max_position=args.max_position,
            long_ex_threshold=Decimal(args.long_threshold),
            short_ex_threshold=Decimal(args.short_threshold)
        )

        # Run the bot
        await bot.run()

    except KeyboardInterrupt:
        print("\nCross-Exchange Arbitrage interrupted by user")
        return 1
    except Exception as e:
        print(f"Error running cross-exchange arbitrage: {e}")
        import traceback
        print(f"Full traceback: {traceback.format_exc()}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
