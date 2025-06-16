import pytest
import os

@pytest.fixture(autouse=True)
def setup_test_environment():
    """设置测试环境"""
    # 创建测试所需的目录
    os.makedirs('logs', exist_ok=True)
    yield
    # 清理测试环境
    # 这里可以添加清理代码 