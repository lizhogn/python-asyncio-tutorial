"""
01. 什么是异步编程？

异步编程是一种编程范式，允许程序在等待某些操作（如网络请求、文件读写）完成时，
可以继续执行其他任务，而不是阻塞等待。

传统同步编程 vs 异步编程的对比
"""

import time
import asyncio


def sync_operation(operation_name, duration):
    """同步操作：会阻塞程序执行"""
    print(f"开始执行 {operation_name}...")
    time.sleep(duration)  # 模拟耗时操作
    print(f"{operation_name} 完成！")
    return f"{operation_name} 的结果"


async def async_operation(operation_name, duration):
    """异步操作：不会阻塞程序执行"""
    print(f"开始执行 {operation_name}...")
    await asyncio.sleep(duration)  # 异步等待
    print(f"{operation_name} 完成！")
    return f"{operation_name} 的结果"


def demo_sync_programming():
    """演示同步编程：操作按顺序执行，总时间 = 所有操作时间之和"""
    print("=== 同步编程演示 ===")
    start_time = time.time()
    
    # 三个同步操作，每个耗时2秒
    result1 = sync_operation("数据库查询", 2)
    result2 = sync_operation("网络请求", 2)
    result3 = sync_operation("文件读取", 2)
    
    end_time = time.time()
    print(f"同步编程总耗时: {end_time - start_time:.2f} 秒")
    print(f"结果: {result1}, {result2}, {result3}")
    print()


async def demo_async_programming():
    """演示异步编程：操作并发执行，总时间 ≈ 最长的单个操作时间"""
    print("=== 异步编程演示 ===")
    start_time = time.time()
    
    # 三个异步操作并发执行，每个耗时2秒
    task1 = asyncio.create_task(async_operation("数据库查询", 2))
    task2 = asyncio.create_task(async_operation("网络请求", 2))
    task3 = asyncio.create_task(async_operation("文件读取", 2))
    
    # 等待所有任务完成
    results = await asyncio.gather(task1, task2, task3)
    
    end_time = time.time()
    print(f"异步编程总耗时: {end_time - start_time:.2f} 秒")
    print(f"结果: {results}")
    print()


async def main():
    """主函数：运行演示"""
    # 先运行同步编程演示
    demo_sync_programming()
    
    # 再运行异步编程演示
    await demo_async_programming()
    
    print("=== 总结 ===")
    print("同步编程：")
    print("- 操作按顺序执行")
    print("- 总时间 = 所有操作时间之和")
    print("- 简单直观，但效率较低")
    print()
    print("异步编程：")
    print("- 操作可以并发执行")
    print("- 总时间 ≈ 最长的单个操作时间")
    print("- 效率更高，但代码复杂度增加")


if __name__ == "__main__":
    # 运行异步主函数
    asyncio.run(main()) 