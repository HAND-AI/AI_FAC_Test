import pytest
import pandas as pd
from src.matching.price_matcher import PriceMatcher

def test_matcher_initialization():
    """测试 PriceMatcher 初始化"""
    matcher = PriceMatcher()
    assert matcher is not None

def test_match_prices():
    """测试价格匹配功能"""
    matcher = PriceMatcher()
    # 创建测试数据
    test_data = pd.DataFrame({
        'SKU': ['TEST001', 'TEST002'],
        'Quantity': [10, 20]
    })
    
    result = matcher.match_prices(test_data)
    assert result is not None
    assert isinstance(result, pd.DataFrame)
    # 验证结果中是否包含必要的列
    assert 'Price' in result.columns 