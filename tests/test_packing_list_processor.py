import pytest
import pandas as pd
from src.processing.packing_list_processor import PackingListProcessor

def test_processor_initialization():
    """测试 PackingListProcessor 初始化"""
    processor = PackingListProcessor()
    assert processor is not None

def test_process_file():
    """测试处理文件功能"""
    processor = PackingListProcessor()
    # 创建测试数据
    test_data = pd.DataFrame({
        'SKU': ['TEST001', 'TEST002'],
        'Quantity': [10, 20]
    })
    
    # 保存测试数据到临时文件
    test_file = 'test_packing_list.xlsx'
    test_data.to_excel(test_file, index=False)
    
    try:
        result = processor.process_file(test_file)
        assert result is not None
        assert isinstance(result, pd.DataFrame)
    finally:
        # 清理测试文件
        import os
        if os.path.exists(test_file):
            os.remove(test_file) 