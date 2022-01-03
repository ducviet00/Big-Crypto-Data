import os
import nltk
nltk.download('vader_lexicon')

from dotenv import load_dotenv

load_dotenv()
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

CRYPTO_SUBS = [
    "bitcoin",
    "CryptoCurrency",
    "btc",
    "CryptoMarkets",
    "bitcoinbeginners",
    "CryptoCurrencies",
    "altcoin",
    "icocrypto",
    "CryptoCurrencyTrading",
    "Crypto_General",
    "ico",
    "blockchain",
    "ethereum",
    "binance",
    "CoinBase",
    "ledgerwallet",
    "defi",
]

SYMBOLS = [
    "BTC/USDT",
    "ETH/USDT",
    "BNB/USDT",
    "NEAR/USDT",
    "ADA/USDT",
    "LTC/USDT",
    "ALICE/USDT",
    "SOL/USDT",
    "XRP/USDT",
    "DOT/USDT",
    "DOGE/USDT",
    "AVAX/USDT",
    "LUNA/USDT",
    "SHIB/USDT",
    "UNI/USDT",
    "BCH/USDT",
    "VET/USDT",
    "XLM/USDT",
    "LINK/USDT",
    "MATIC/USDT",
    "ATOM/USDT",
]