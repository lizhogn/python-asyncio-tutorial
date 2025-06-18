"""
exercises/01_basic_exercises_solutions.py

Asyncio 基础练习参考答案

这是练习的参考答案，展示了正确的实现方式。
建议先尝试自己完成练习，然后再查看答案。
"""

import asyncio
import time
import random


# 练习 1 参考答案
async def greet_person(name, delay):
    """练习1：问候协程"""
    print(f"Hello, {name}!")
    await asyncio.sleep(delay)
    print(f"Goodbye, {name}!")


# 练习 2 参考答案
async def run_multiple_greetings():
    """练习2：并发执行多个问候"""
    # 方法1: 使用 asyncio.gather()
    await asyncio.gather(
        greet_person("Alice", 1),
        greet_person("Bob", 2),
        greet_person("Charlie", 1.5)
    )
    
    # 方法2: 使用 asyncio.create_task()
    # tasks = [
    #     asyncio.create_task(greet_person("Alice", 1)),
    #     asyncio.create_task(greet_person("Bob", 2)),
    #     asyncio.create_task(greet_person("Charlie", 1.5))
    # ]
    # await asyncio.gather(*tasks)


# 练习 3 参考答案
async def get_user_info(user_id):
    """练习3：获取用户信息"""
    await asyncio.sleep(1)  # 模拟网络请求
    return {
        "id": user_id,
        "name": f"用户{user_id}",
        "email": f"user{user_id}@example.com"
    }


# 练习 4 参考答案
async def risky_operation():
    """练习4：可能失败的操作"""
    await asyncio.sleep(0.5)  # 模拟处理时间
    if random.random() < 0.5:
        raise ValueError("随机错误发生了！")
    return "操作成功"


async def safe_operation():
    """练习4：安全的操作调用"""
    try:
        result = await risky_operation()
        print(f"操作成功: {result}")
        return result
    except ValueError as e:
        print(f"操作失败: {e}")
        return None


# 练习 5 参考答案
async def slow_operation():
    """练习5：慢速操作"""
    print("开始慢速操作...")
    await asyncio.sleep(5)  # 模拟耗时操作
    print("慢速操作完成")
    return "慢速操作结果"


async def timeout_demo():
    """练习5：超时演示"""
    try:
        result = await asyncio.wait_for(slow_operation(), timeout=3.0)
        print(f"操作结果: {result}")
    except asyncio.TimeoutError:
        print("操作超时！")


# 练习 6 参考答案
class DatabaseConnection:
    """练习6：数据库连接上下文管理器"""
    
    async def __aenter__(self):
        """进入上下文时调用"""
        print("连接数据库")
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """退出上下文时调用"""
        print("关闭数据库连接")
        return False  # 不抑制异常


async def use_database():
    """练习6：使用数据库连接"""
    async with DatabaseConnection():
        print("执行数据库操作...")
        await asyncio.sleep(1)  # 模拟数据库操作
        print("数据库操作完成")


# 练习 7 参考答案
async def fibonacci_generator(n):
    """练习7：斐波那契数列生成器"""
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b
        await asyncio.sleep(0.1)  # 每个数字之间等待0.1秒


async def use_fibonacci():
    """练习7：使用斐波那契生成器"""
    print("斐波那契数列:")
    async for num in fibonacci_generator(10):
        print(num, end=" ")
    print()


# 额外练习：信号量示例
async def semaphore_demo():
    """信号量演示：限制并发数量"""
    semaphore = asyncio.Semaphore(2)  # 最多同时执行2个任务
    
    async def limited_task(name, delay):
        async with semaphore:
            print(f"{name} 开始执行")
            await asyncio.sleep(delay)
            print(f"{name} 完成")
    
    tasks = [
        limited_task(f"任务{i}", i)
        for i in range(1, 6)
    ]
    
    await asyncio.gather(*tasks)


# 额外练习：事件循环监控
async def loop_monitoring_demo():
    """事件循环监控演示"""
    loop = asyncio.get_event_loop()
    
    async def monitored_task(name, delay):
        start_time = time.time()
        print(f"{name} 开始")
        await asyncio.sleep(delay)
        end_time = time.time()
        print(f"{name} 完成，耗时: {end_time - start_time:.2f}秒")
    
    tasks = [
        monitored_task(f"监控任务{i}", i)
        for i in range(1, 4)
    ]
    
    await asyncio.gather(*tasks)


async def main():
    """运行所有练习的参考答案"""
    print("=== Asyncio 基础练习参考答案 ===\n")
    
    # 运行练习1
    print("练习1: 简单协程")
    await greet_person("Alice", 1)
    print()
    
    # 运行练习2
    print("练习2: 并发执行")
    await run_multiple_greetings()
    print()
    
    # 运行练习3
    print("练习3: 带返回值的协程")
    user_info = await get_user_info(123)
    print(f"用户信息: {user_info}")
    print()
    
    # 运行练习4
    print("练习4: 异常处理")
    await safe_operation()
    print()
    
    # 运行练习5
    print("练习5: 超时处理")
    await timeout_demo()
    print()
    
    # 运行练习6
    print("练习6: 异步上下文管理器")
    await use_database()
    print()
    
    # 运行练习7
    print("练习7: 异步生成器")
    await use_fibonacci()
    print()
    
    # 额外练习
    print("额外练习: 信号量演示")
    await semaphore_demo()
    print()
    
    print("额外练习: 事件循环监控")
    await loop_monitoring_demo()
    print()
    
    print("所有参考答案演示完成！")


if __name__ == "__main__":
    # 运行参考答案
    asyncio.run(main()) 