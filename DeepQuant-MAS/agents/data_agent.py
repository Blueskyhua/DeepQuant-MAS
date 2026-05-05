import logging
import random

logger = logging.getLogger("Data-Agent")

class DataAgent:
    def __init__(self):
        logger.info("Data Agent initialized.")

    def fetch_data(self, symbol):
        logger.info(f"Fetching OHLCV and news for {symbol}")
        # 模拟返回的 K 线数据字典和一条新闻
        mock_market_data = {
            "price": random.uniform(100, 500),
            "volume": random.randint(1000, 50000),
            "RSI": random.uniform(20, 80)
        }
        mock_news = f"Breaking news regarding {symbol}: Latest earnings report shows unexpected shifts in revenue."
        return mock_market_data, mock_news