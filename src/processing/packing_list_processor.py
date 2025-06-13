import pandas as pd
from loguru import logger

class PackingListProcessor:
    def __init__(self):
        self.required_columns = ['Item Code', 'Quantity']
        
    def process_file(self, file_path):
        """
        处理打包清单Excel文件
        
        Args:
            file_path (str): Excel文件路径
            
        Returns:
            pd.DataFrame: 处理后的数据，如果处理失败则返回None
        """
        try:
            # 读取Excel文件
            df = pd.read_excel(file_path)
            
            # 验证必需列
            if not self._validate_columns(df):
                return None
                
            # 清理数据
            df = self._clean_data(df)
            
            return df
            
        except Exception as e:
            logger.exception(f"处理文件时发生错误: {str(e)}")
            return None
            
    def _validate_columns(self, df):
        """验证数据框是否包含所有必需的列"""
        missing_columns = [col for col in self.required_columns if col not in df.columns]
        if missing_columns:
            logger.error(f"缺少必需的列: {', '.join(missing_columns)}")
            return False
        return True
        
    def _clean_data(self, df):
        """清理数据"""
        # 删除空行
        df = df.dropna(subset=['Item Code'])
        
        # 确保数量为数值类型
        df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
        
        # 删除数量为0或负数的行
        df = df[df['Quantity'] > 0]
        
        return df 