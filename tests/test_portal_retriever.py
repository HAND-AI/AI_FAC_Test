import pytest
from src.retrieval.portal_retriever import PortalRetriever

def test_portal_retriever_initialization():
    """测试 PortalRetriever 初始化"""
    retriever = PortalRetriever()
    assert retriever is not None
def test_get_latest_packing_list():
    """测试获取最新打包清单"""
    retriever = PortalRetriever()
    # 注意：这个测试可能需要模拟网络请求
    # 在实际测试中，您可能需要使用 pytest-mock 来模拟网络请求
    with pytest.raises(Exception):
        retriever.get_latest_packing_list() 

