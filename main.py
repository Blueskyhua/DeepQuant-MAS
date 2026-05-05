import time
import logging
from agents.data_agent import DataAgent
from agents.reasoning_agent import ReasoningAgent
from agents.execution_agent import ExecutionAgent

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("System-Orchestrator")


def main():
    logger.info("Initializing DeepQuant Multi-Agent System...")

    # 初始化各 Agent
    data_agent = DataAgent()
    reasoning_agent = ReasoningAgent()
    execution_agent = ExecutionAgent()

    symbols = ["AAPL", "TSLA", "BTC-USD"]

    try:
        while True:
            logger.info("--- Starting new analysis cycle ---")
            for symbol in symbols:
                logger.info(f"Processing symbol: {symbol}")

                # 1. Data Agent 拉取数据
                market_data, latest_news = data_agent.fetch_data(symbol)

                # 2. Reasoning Agent 长链推理情绪
                sentiment_score, reasoning_chain = reasoning_agent.analyze_sentiment(latest_news)

                # 3. Execution Agent 深度学习预测与决策
                decision = execution_agent.make_decision(symbol, market_data, sentiment_score)

                logger.info(
                    f"Final Decision for {symbol}: {decision['action']} | Size: {decision['size']} | Confidence: {decision['confidence']}%")

            logger.info("Cycle complete. Sleeping for 15 minutes...")
            time.sleep(900)  # 每 15 分钟执行一次

    except KeyboardInterrupt:
        logger.info("System gracefully shut down by user.")


if __name__ == "__main__":
    main()