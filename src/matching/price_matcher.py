import os
import pandas as pd
from datetime import datetime
from loguru import logger

class PriceMatcher:
    def __init__(self):
        self.price_list_dir = os.path.join('data', 'price_list')
        
    def match_prices(self, packing_list_data):
        """
        将打包清单数据与价格表匹配
        
        Args:
            packing_list_data (pd.DataFrame): 打包清单数据
            
        Returns:
            pd.DataFrame: 匹配后的数据，如果匹配失败则返回None
        """
        try:
            # 获取最新的价格表
            price_list_path = self._get_latest_price_list()
            if not price_list_path:
                logger.error("未找到价格表文件")
                return None
                
            # 读取价格表
            price_df = pd.read_excel(price_list_path)
            
            # 合并数据
            merged_df = pd.merge(
                packing_list_data,
                price_df[['Item Code', 'Unit Price']],
                on='Item Code',
                how='left'
            )
            
            # 计算总价
            merged_df['Total'] = merged_df['Quantity'] * merged_df['Unit Price']
            
            # 记录未匹配的项目
            unmatched = merged_df[merged_df['Unit Price'].isna()]
            if not unmatched.empty:
                logger.warning(f"发现{len(unmatched)}个未匹配的项目")
                self._log_unmatched_items(unmatched)
                
            return merged_df
            
        except Exception as e:
            logger.exception(f"价格匹配时发生错误: {str(e)}")
            return None
            
    def _get_latest_price_list(self):
        """获取最新的价格表文件路径"""
        try:
            files = [f for f in os.listdir(self.price_list_dir) if f.endswith('.xlsx')]
            if not files:
                return None
                
            # 按修改时间排序
            latest_file = max(
                files,
                key=lambda x: os.path.getmtime(os.path.join(self.price_list_dir, x))
            )
            return os.path.join(self.price_list_dir, latest_file)
            
        except Exception as e:
            logger.exception(f"获取最新价格表时发生错误: {str(e)}")
            return None
            
    def _log_unmatched_items(self, unmatched_df):
        """记录未匹配的项目"""
        log_path = os.path.join('logs', f'unmatched_items_{datetime.now().strftime("%Y%m%d")}.txt')
        unmatched_df.to_csv(log_path, index=False)
        logger.info(f"未匹配项目已记录到: {log_path}") 