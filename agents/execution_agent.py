import logging

logger = logging.getLogger("Execution-Agent")


class ExecutionAgent:
    def __init__(self):
        logger.info("Execution Agent initialized. Loading Transformer model weights...")
        # 实际这里会加载 PyTorch/TensorFlow 模型： self.model = load_model("weights.pth")

    def make_decision(self, symbol, market_data, sentiment_score):
        logger.info("Fusing Deep Learning technical predictions with LLM sentiment...")

        # 假设简单的逻辑：情绪 > 0.5 且 RSI < 70 则买入
        if sentiment_score > 0.3 and market_data['RSI'] < 60:
            action = "BUY"
            size = 100
            confidence = 85
        elif sentiment_score < -0.3 and market_data['RSI'] > 40:
            action = "SELL"
            size = 100
            confidence = 90
        else:
            action = "HOLD"
            size = 0
            confidence = 50

        return {
            "action": action,
            "size": size,
            "confidence": confidence
        }