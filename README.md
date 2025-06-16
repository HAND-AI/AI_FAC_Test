# 打包清单自动化系统

## 系统概述

本系统用于自动化处理打包清单，包括从在线门户获取文件、解析Excel数据、匹配价格信息，并生成最终报告。

## 功能特点

- 自动从指定门户下载最新的打包清单
- 自动解析和验证Excel数据
- 与最新价格表进行匹配
- 生成详细的处理报告和错误日志
- 支持多种数据格式和错误处理

## 安装要求

- Python 3.8+
- Chrome浏览器（用于网页自动化）
- 相关Python包（见requirements.txt）

## 安装步骤

1. 克隆仓库：
```bash
git clone [repository_url]
cd [repository_name]
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

3. 配置环境变量：
创建`.env`文件并设置以下变量：
```
PORTAL_A_USERNAME=your_username
PORTAL_A_PASSWORD=your_password
PORTAL_B_USERNAME=your_username
PORTAL_B_PASSWORD=your_password
```

## 目录结构

```
.
├── data/
│   ├── packing_lists/    # 下载的打包清单
│   ├── price_list/       # 价格表文件
│   └── output/           # 输出结果
├── logs/                 # 日志文件
├── src/
│   ├── retrieval/        # 文件获取模块
│   ├── processing/       # 数据处理模块
│   ├── matching/         # 价格匹配模块
│   └── output/          # 结果输出模块
├── main.py              # 主程序
└── requirements.txt     # 依赖列表
```

## 使用方法

1. 确保价格表已放置在`data/price_list/`目录下

2. 运行主程序：
```bash
python main.py
```

3. 查看输出：
- 处理结果将保存在`data/output/`目录
- 日志文件将保存在`logs/`目录
- 未匹配项目将记录在`logs/unmatched_items_[date].txt`

## 错误处理

系统会自动处理以下情况：
- 缺少必需的数据列
- 价格表文件不存在
- 项目代码未匹配
- 数据格式错误

所有错误都会记录在日志文件中，并生成相应的错误报告。

## 注意事项

- 确保网络连接稳定
- 定期更新价格表
- 检查日志文件以监控系统运行状态
- 及时处理未匹配的项目 