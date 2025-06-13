import os
from datetime import datetime
from loguru import logger
from src.retrieval.portal_retriever import PortalRetriever
from src.processing.packing_list_processor import PackingListProcessor
from src.matching.price_matcher import PriceMatcher
from src.output.result_writer import ResultWriter

def setup_logging():
    """设置日志配置"""
    log_path = os.path.join('logs', f'packing_list_{datetime.now().strftime("%Y%m%d")}.log')
    logger.add(log_path, rotation="1 day", retention="7 days")

def main():
    try:
        # 设置日志
        setup_logging()
        logger.info("开始处理打包清单")

        # 1. 检测并下载最新的打包清单
        retriever = PortalRetriever()
        packing_list_path = retriever.get_latest_packing_list()
        if not packing_list_path:
            logger.error("未找到打包清单文件")
            return

        # 2. 处理打包清单数据
        processor = PackingListProcessor()
        packing_list_data = processor.process_file(packing_list_path)
        if packing_list_data is None:
            logger.error("处理打包清单失败")
            return

        # 3. 匹配价格
        matcher = PriceMatcher()
        matched_data = matcher.match_prices(packing_list_data)
        if matched_data is None:
            logger.error("价格匹配失败")
            return

        # 4. 输出结果
        writer = ResultWriter()
        output_path = writer.write_results(matched_data)
        
        logger.info(f"处理完成，结果已保存至: {output_path}")

    except Exception as e:
        logger.exception(f"处理过程中发生错误: {str(e)}")
        raise

if __name__ == "__main__":
    main()
