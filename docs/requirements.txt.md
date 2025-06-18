# 项目依赖

## 基础包（Python 3.7+ 内置）

- **asyncio** - 异步编程库（内置）
- **aiofiles** - 异步文件操作

## 网络请求

- **aiohttp** >= 3.8.0 - 异步 HTTP 客户端/服务器框架
- **requests** >= 2.28.0 - HTTP 库（用于对比）

## 数据库（可选）

- **aiosqlite** >= 0.17.0 - 异步 SQLite 驱动

## 工具包

- **python-dateutil** >= 2.8.0 - 日期时间工具

## 开发工具（可选）

- **pytest** >= 7.0.0 - 测试框架
- **pytest-asyncio** >= 0.21.0 - asyncio 测试支持

## 安装方法

```bash
# 安装所有依赖
pip install -r requirements.txt

# 或者单独安装
pip install aiohttp requests aiofiles
```

## 版本要求

- **Python**: >= 3.7（推荐 3.8+）
- **操作系统**: 跨平台支持

## 注意事项

1. 确保使用 Python 3.7 或更高版本
2. 建议在虚拟环境中安装依赖
3. 某些示例可能需要网络连接
4. 异步网络请求示例需要安装 aiohttp 