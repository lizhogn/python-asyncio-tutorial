"""
exercises/01_basic_exercises.py

Asyncio 基础练习

这些练习将帮助你巩固 asyncio 的基础概念。
请尝试完成每个练习，然后查看参考答案。
"""

import asyncio
import time


# 练习 1: 创建简单的协程
"""
任务：创建一个协程函数，它接受一个名字和延迟时间，
然后打印 "Hello, {name}!"，等待指定的延迟时间，
最后打印 "Goodbye, {name}!"

提示：使用 async def 和 await asyncio.sleep()
"""

# TODO: 在这里实现你的协程函数
async def greet_person(name, delay):
    """练习1：问候协程"""
    # 你的代码在这里
    pass


# 练习 2: 并发执行多个协程
"""
任务：创建一个函数，并发执行多个问候协程，
并等待所有协程完成。

提示：使用 asyncio.gather() 或 asyncio.create_task()
"""

async def run_multiple_greetings():
    """练习2：并发执行多个问候"""
    # 你的代码在这里
    pass


# 练习 3: 带返回值的协程
"""
任务：创建一个协程函数，模拟获取用户信息。
它应该接受用户ID，等待1秒，然后返回一个字典，
包含用户ID、姓名和邮箱。

提示：使用 return 语句返回数据
"""

async def get_user_info(user_id):
    """练习3：获取用户信息"""
    # 你的代码在这里
    pass


# 练习 4: 协程中的异常处理
"""
任务：创建一个协程函数，它可能随机失败。
如果随机数小于0.5，抛出异常；否则返回成功消息。
在调用这个协程时，正确处理异常。

提示：使用 try/except 和 random.random()
"""

async def risky_operation():
    """练习4：可能失败的操作"""
    # 你的代码在这里
    pass


async def safe_operation():
    """练习4：安全的操作调用"""
    # 你的代码在这里
    pass


# 练习 5: 超时处理
"""
任务：创建一个协程函数，它需要很长时间才能完成。
在调用时设置超时时间，如果超时就取消任务。

提示：使用 asyncio.wait_for() 和 asyncio.TimeoutError
"""

async def slow_operation():
    """练习5：慢速操作"""
    # 你的代码在这里
    pass


async def timeout_demo():
    """练习5：超时演示"""
    # 你的代码在这里
    pass


# 练习 6: 自定义异步上下文管理器
"""
任务：创建一个异步上下文管理器，用于模拟数据库连接。
在进入时打印 "连接数据库"，在退出时打印 "关闭数据库连接"。

提示：使用 async def __aenter__() 和 async def __aexit__()
"""

class DatabaseConnection:
    """练习6：数据库连接上下文管理器"""
    # 你的代码在这里
    pass


async def use_database():
    """练习6：使用数据库连接"""
    # 你的代码在这里
    pass


# 练习 7: 异步生成器
"""
任务：创建一个异步生成器，生成斐波那契数列的前N个数。
每个数字之间等待0.1秒。

提示：使用 async def 和 yield
"""

async def fibonacci_generator(n):
    """练习7：斐波那契数列生成器"""
    # 你的代码在这里
    pass


async def use_fibonacci():
    """练习7：使用斐波那契生成器"""
    # 你的代码在这里
    pass


# 主函数：运行所有练习
async def main():
    """运行所有练习"""
    print("=== Asyncio 基础练习 ===\n")
    
    # 运行练习1
    print("练习1: 简单协程")
    # await greet_person("Alice", 1)
    print()
    
    # 运行练习2
    print("练习2: 并发执行")
    # await run_multiple_greetings()
    print()
    
    # 运行练习3
    print("练习3: 带返回值的协程")
    # user_info = await get_user_info(123)
    # print(f"用户信息: {user_info}")
    print()
    
    # 运行练习4
    print("练习4: 异常处理")
    # await safe_operation()
    print()
    
    # 运行练习5
    print("练习5: 超时处理")
    # await timeout_demo()
    print()
    
    # 运行练习6
    print("练习6: 异步上下文管理器")
    # await use_database()
    print()
    
    # 运行练习7
    print("练习7: 异步生成器")
    # await use_fibonacci()
    print()
    
    print("所有练习完成！")


if __name__ == "__main__":
    # 运行练习
    asyncio.run(main()) 