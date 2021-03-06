from asyncio.tasks import sleep
import os
import sys
from asyncio import gather, get_event_loop
from datetime import datetime

from kafka_producer import producer

from config import SYMBOLS

# -----------------------------------------------------------------------------

this_folder = os.path.dirname(os.path.abspath("."))
root_folder = os.path.dirname(os.path.dirname(this_folder))
sys.path.append(root_folder + "/python")
sys.path.append(this_folder)

# -----------------------------------------------------------------------------

import ccxt.async_support as ccxt  # noqa: E402

# -----------------------------------------------------------------------------


print("CCXT Version:", ccxt.__version__)

class BinanceCrawler():
    def __init__(self, producer, symbols, timeframe="1m", limit=1000):
        self.exchange = ccxt.binance()
        self.timeframe = timeframe
        self.limit = limit
        self.symbols = symbols
        self.producer = producer


    def send_data(self, candles, trading_pair):

        ticker = trading_pair.split("/")[0].upper()
        for candle in candles:
            candle["ticker"] = ticker
        self.producer.send(topic="_TradingData", value=candles)

    def to_json(self, candles):
        data = []
        for ohlcv in candles:
            data.append(
                {
                    "Date": datetime.fromtimestamp(ohlcv[0] // 1000).isoformat(),
                    "Open": ohlcv[1],
                    "High": ohlcv[2],
                    "Low": ohlcv[3],
                    "Close": ohlcv[4],
                    "Volume": ohlcv[5],
                }
            )
        return data


    async def fetch_ohlcv(self, symbol):
        since = self.exchange.parse8601("2017-08-17T00:00:00Z")
        timeframe_duration_in_seconds = self.exchange.parse_timeframe(self.timeframe)
        timeframe_duration_in_ms = timeframe_duration_in_seconds * 1000
        timedelta = self.limit * timeframe_duration_in_ms
        fetch_since = since
        while True:
            try:
                candles = await self.exchange.fetch_ohlcv(symbol, self.timeframe, fetch_since, self.limit)

                fetch_since = (
                    (candles[-1][0] + 1) if len(candles) else (fetch_since + timedelta)
                )
                if fetch_since:
                    print(fetch_since, symbol)
                candles_json = self.to_json(candles)
                self.send_data(candles_json, symbol)
                await sleep(0.05)
            except Exception as e:
                print(type(e).__name__, str(e))

    async def run(self):
        loops = [self.fetch_ohlcv(symbol) for symbol in self.symbols]
        await gather(*loops)
        await self.exchange.close()

if __name__ == "__main__":
    binance = BinanceCrawler(producer, SYMBOLS)
    loop = get_event_loop()
    loop.run_until_complete(binance.run())