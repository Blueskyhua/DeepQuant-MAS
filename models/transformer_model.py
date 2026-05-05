import torch
import torch.nn as nn

class TradingTransformer(nn.Module):
    """
    专门用于处理时序价格数据的 Transformer 编码器模型
    """
    def __init__(self, input_dim=5, embed_dim=64, num_heads=4, num_layers=2):
        super(TradingTransformer, self).__init__()
        self.embedding = nn.Linear(input_dim, embed_dim)
        # 定义 Transformer 编码器层
        encoder_layer = nn.TransformerEncoderLayer(d_model=embed_dim, nhead=num_heads)
        self.transformer_encoder = nn.TransformerEncoder(encoder_layer, num_layers=num_layers)
        self.fc_out = nn.Linear(embed_dim, 1) # 输出预测价格或涨跌概率

    def forward(self, x):
        # x shape: (sequence_length, batch_size, input_dim)
        x = self.embedding(x)
        x = self.transformer_encoder(x)
        return self.fc_out(x[-1, :, :]) # 取最后一个时间步的结果
