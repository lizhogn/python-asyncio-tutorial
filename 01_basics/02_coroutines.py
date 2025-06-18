"""
02. 协程（Coroutines）

协程是 asyncio 的核心概念，它是一种可以暂停和恢复执行的函数。
使用 async def 定义的函数就是协程函数，调用协程函数会返回协程对象。

关键概念：
- async def: 定义协程函数
- await: 等待协程完成
- 协程对象: 调用协程函数返回的对象
"""

import asyncio
import time


# 1. 基本的协程函数
async def hello_world():
    """最简单的协程函数"""
    print("Hello")
    await asyncio.sleep(1)  # 异步等待1秒
    print("World")


# 2. 带返回值的协程函数
async def get_user_info(user_id):
    """模拟获取用户信息的协程"""
    print(f"正在获取用户 {user_id} 的信息...")
    await asyncio.sleep(1)  # 模拟网络请求
    return {"id": user_id, "name": f"用户{user_id}", "email": f"user{user_id}@example.com"}


# 3. 嵌套协程调用
async def process_user(user_id):
    """处理用户的协程，内部调用其他协程"""
    print(f"开始处理用户 {user_id}")
    
    # 获取用户信息
    user_info = await get_user_info(user_id)
    
    # 模拟其他处理
    await asyncio.sleep(0.5)
    
    print(f"用户 {user_id} 处理完成: {user_info}")
    return user_info


# 4. 协程中的异常处理
async def risky_operation():
    """可能出错的协程"""
    await asyncio.sleep(1)
    # 模拟随机错误
    import random
    if random.random() < 0.5:
        raise ValueError("随机错误发生了！")
    return "操作成功"


async def safe_operation():
    """安全的协程，包含异常处理"""
    try:
        result = await risky_operation()
        print(f"操作结果: {result}")
        return result
    except ValueError as e:
        print(f"捕获到错误: {e}")
        return None


# 5. 协程的状态
async def demonstrate_coroutine_states():
    """演示协程的不同状态"""
    print("=== 协程状态演示 ===")
    
    # 创建协程对象（此时还未开始执行）
    coro = get_user_info(1)
    print(f"协程对象: {coro}")
    print(f"协程类型: {type(coro)}")
    
    # 执行协程
    result = await coro
    print(f"协程执行结果: {result}")
    print()


# 6. 协程与普通函数的对比
def sync_function():
    """同步函数"""
    print("这是同步函数")
    time.sleep(1)  # 阻塞等待
    print("同步函数完成")
    return "同步结果"


async def async_function():
    """异步函数（协程）"""
    print("这是异步函数")
    await asyncio.sleep(1)  # 非阻塞等待
    print("异步函数完成")
    return "异步结果"


async def compare_sync_async():
    """对比同步和异步函数"""
    print("=== 同步 vs 异步函数对比 ===")
    
    print("执行同步函数:")
    start = time.time()
    sync_result = sync_function()
    sync_time = time.time() - start
    print(f"同步函数耗时: {sync_time:.2f} 秒")
    
    print("\n执行异步函数:")
    start = time.time()
    async_result = await async_function()
    async_time = time.time() - start
    print(f"异步函数耗时: {async_time:.2f} 秒")
    
    print(f"\n结果对比:")
    print(f"同步结果: {sync_result}")
    print(f"异步结果: {async_result}")


async def main():
    """主函数：演示各种协程概念"""
    print("=== 协程基础概念演示 ===\n")
    
    # 1. 基本协程
    print("1. 基本协程:")
    await hello_world()
    print()
    
    # 2. 带返回值的协程
    print("2. 带返回值的协程:")
    user_info = await get_user_info(123)
    print(f"获取到的用户信息: {user_info}")
    print()
    
    # 3. 嵌套协程
    print("3. 嵌套协程调用:")
    await process_user(456)
    print()
    
    # 4. 异常处理
    print("4. 协程异常处理:")
    await safe_operation()
    print()
    
    # 5. 协程状态
    await demonstrate_coroutine_states()
    
    # 6. 同步 vs 异步对比
    await compare_sync_async()
    
    print("\n=== 重要概念总结 ===")
    print("1. async def 定义协程函数")
    print("2. await 等待协程完成")
    print("3. 协程可以暂停和恢复执行")
    print("4. 协程不会阻塞事件循环")
    print("5. 协程可以嵌套调用")
    print("6. 协程支持异常处理")


if __name__ == "__main__":
    # 运行主协程
    asyncio.run(main()) 