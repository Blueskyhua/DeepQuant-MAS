# DeepQuant-MAS 📈🤖

DeepQuant Multi-Agent System (DQ-MAS) is a cooperative quantitative trading framework driven by Deep Learning and Large Language Models (LLM). 

## Architecture
- **Data Agent**: Fetches real-time OHLCV data and financial news.
- **Reasoning Agent (LLM)**: Uses long-chain reasoning to extract sentiment factors from unstructured news text.
- **Execution Agent (DL)**: Combines LLM sentiment scores with Time-Series Transformer predictions to make final trading decisions.

## Quick Start
```bash
pip install -r requirements.txt
export OPENAI_API_KEY="your_api_key_here"
python main.py