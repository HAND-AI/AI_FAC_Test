import pytest
import pandas as pd
import os
from src.output.result_writer import ResultWriter

def test_writer_initialization():
    """测试 ResultWriter 初始化"""
    writer = ResultWriter()
    assert writer is not None

def test_write_results():
    """测试结果写入功能"""
    writer = ResultWriter()
    # 创建测试数据
    test_data = pd.DataFrame({
        'SKU': ['TEST001', 'TEST002'],
        'Quantity': [10, 20],
        'Price': [100, 200]
    })
    
    output_path = writer.write_results(test_data)
    assert output_path is not None
    assert os.path.exists(output_path)
    
    # 清理测试文件
    if os.path.exists(output_path):
        os.remove(output_path) 