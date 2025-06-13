import os
from datetime import datetime
from loguru import logger

class ResultWriter:
    def __init__(self):
        self.output_dir = os.path.join('data', 'output')
        os.makedirs(self.output_dir, exist_ok=True)
        
    def write_results(self, data):
        """
        将处理结果写入文件
        
        Args:
            data (pd.DataFrame): 处理后的数据
            
        Returns:
            str: 输出文件路径，如果写入失败则返回None
        """
        try:
            # 生成输出文件名
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = os.path.join(self.output_dir, f'packing_list_result_{timestamp}.xlsx')
            
            # 写入Excel文件
            data.to_excel(output_file, index=False)
            
            # 生成汇总报告
            self._generate_summary(data, output_file)
            
            logger.info(f"结果已保存到: {output_file}")
            return output_file
            
        except Exception as e:
            logger.exception(f"写入结果时发生错误: {str(e)}")
            return None
            
    def _generate_summary(self, data, output_file):
        """生成处理汇总报告"""
        try:
            summary = {
                "总项目数": len(data),
                "总数量": data['Quantity'].sum(),
                "总金额": data['Total'].sum(),
                "未匹配项目数": data['Unit Price'].isna().sum()
            }
            
            # 将汇总信息写入日志
            logger.info("处理汇总:")
            for key, value in summary.items():
                logger.info(f"{key}: {value}")
                
        except Exception as e:
            logger.exception(f"生成汇总报告时发生错误: {str(e)}") 