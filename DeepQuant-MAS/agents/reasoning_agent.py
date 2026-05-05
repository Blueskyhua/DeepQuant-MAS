import logging
import random

logger = logging.getLogger("Reasoning-Agent")


class ReasoningAgent:
    def __init__(self):
        self.system_prompt = """
        You are an expert financial analyst Agent. 
        Perform step-by-step reasoning on the provided news:
        1. Extract the core event.
        2. Analyze macroeconomic and industry-specific impact.
        3. Deduce the bullish or bearish sentiment.
        4. Output a final sentiment score between -1.0 (Extreme Bearish) to 1.0 (Extreme Bullish).
        """
        logger.info("Reasoning Agent initialized with Long-Chain Prompts.")

    def analyze_sentiment(self, news_text):
        logger.info(f"Analyzing news: '{news_text[:30]}...'")

        # 实际项目中这里将调用 LLM API (如 OpenAI, DeepSeek, 智谱等)
        # response = llm_client.chat.completions.create(...)

        # 这里用模拟输出展示多步推理过程
        mock_reasoning_chain = (
            "Step 1: Company announced unexpected CEO departure. "
            "Step 2: This creates leadership uncertainty in a highly competitive quarter. "
            "Step 3: Market sentiment shifts to panic. "
            "Step 4: Score: -0.65"
        )

        mock_score = random.uniform(-1.0, 1.0)
        logger.info(f"Reasoning completed. Sentiment Score: {mock_score:.2f}")

        return mock_score, mock_reasoning_chain