# Task 对象

Task 是 asyncio 中表示协程执行状态的对象，它是对协程的包装。Task 对象提供了更丰富的功能，如取消、状态查询、异常处理等。

## 关键概念

- Task 是对协程的包装
- Task 可以并发执行
- Task 可以被取消
- Task 有执行状态

## 创建 Task 的基本方法

```python
import asyncio
import time
from datetime import datetime

async def simple_task(name, delay):
    """简单的任务函数"""
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {name} 开始")
    await asyncio.sleep(delay)
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {name} 完成")
    return f"{name} 的结果"

async def basic_task_demo():
    """演示创建 Task 的基本方法"""
    print("=== Task 创建方法演示 ===")
    
    # 方法1: asyncio.create_task() (推荐)
    print("方法1: asyncio.create_task()")
    task1 = asyncio.create_task(simple_task("任务1", 2))
    print(f"Task 对象: {task1}")
    print(f"Task 是否完成: {task1.done()}")
    
    # 等待任务完成
    result1 = await task1
    print(f"Task 结果: {result1}")
    print(f"Task 是否完成: {task1.done()}")
    
    # 方法2: 直接 await 协程
    print("方法2: 直接 await 协程")
    result2 = await simple_task("任务2", 1)
    print(f"协程结果: {result2}")
```

## Task 的状态和属性

```python
async def task_status_demo():
    """演示 Task 的状态和属性"""
    print("=== Task 状态演示 ===")
    
    async def status_task(name, delay):
        """用于演示状态的任务"""
        print(f"{name} 开始执行")
        await asyncio.sleep(delay)
        print(f"{name} 执行完成")
        return f"{name} 的返回值"
    
    # 创建任务
    task = asyncio.create_task(status_task("状态任务", 2))
    
    # 检查任务状态
    print(f"Task 对象: {task}")
    print(f"是否完成: {task.done()}")
    print(f"是否取消: {task.cancelled()}")
    print(f"是否正在运行: {not task.done()}")
    
    # 等待任务完成
    result = await task
    
    print(f"任务完成后的状态:")
    print(f"是否完成: {task.done()}")
    print(f"是否取消: {task.cancelled()}")
    print(f"任务结果: {result}")
    print(f"任务异常: {task.exception()}")
```

## Task 的取消功能

```python
async def task_cancellation_demo():
    """演示如何取消 Task"""
    print("=== Task 取消演示 ===")
    
    async def cancellable_task(name, duration):
        """可以被取消的任务"""
        try:
            print(f"{name} 开始执行")
            await asyncio.sleep(duration)
            print(f"{name} 正常完成")
            return f"{name} 成功"
        except asyncio.CancelledError:
            print(f"{name} 被取消")
            raise  # 重新抛出取消异常
    
    # 创建长时间运行的任务
    task = asyncio.create_task(cancellable_task("长时间任务", 10))
    
    # 等待一段时间后取消
    await asyncio.sleep(1)
    print("准备取消任务...")
    
    # 取消任务
    task.cancel()
    
    try:
        await task
    except asyncio.CancelledError:
        print("任务已被取消")
    
    print(f"任务是否取消: {task.cancelled()}")
```

## 并发执行多个 Task

```python
async def concurrent_tasks_demo():
    """演示并发执行多个 Task"""
    print("=== 并发 Task 演示 ===")
    
    async def concurrent_task(name, delay):
        """并发任务"""
        print(f"[{datetime.now().strftime('%H:%M:%S')}] {name} 开始")
        await asyncio.sleep(delay)
        print(f"[{datetime.now().strftime('%H:%M:%S')}] {name} 完成")
        return f"{name} 的结果"
    
    # 创建多个任务
    tasks = [
        asyncio.create_task(concurrent_task(f"任务{i}", i))
        for i in range(1, 4)
    ]
    
    print("所有任务已创建，开始并发执行...")
    start_time = time.time()
    
    # 等待所有任务完成
    results = await asyncio.gather(*tasks)
    
    end_time = time.time()
    print(f"所有任务完成，总耗时: {end_time - start_time:.2f} 秒")
    print(f"任务结果: {results}")
```

## Task 的异常处理

```python
async def task_exception_demo():
    """演示 Task 的异常处理"""
    print("=== Task 异常处理演示 ===")
    
    async def failing_task(name):
        """会失败的任务"""
        print(f"{name} 开始执行")
        await asyncio.sleep(1)
        raise ValueError(f"{name} 执行失败")
    
    async def successful_task(name):
        """成功的任务"""
        print(f"{name} 开始执行")
        await asyncio.sleep(0.5)
        return f"{name} 成功"
    
    # 创建任务
    task1 = asyncio.create_task(successful_task("成功任务"))
    task2 = asyncio.create_task(failing_task("失败任务"))
    
    # 等待任务完成并处理异常
    try:
        result1 = await task1
        print(f"成功任务结果: {result1}")
    except Exception as e:
        print(f"成功任务异常: {e}")
    
    try:
        result2 = await task2
        print(f"失败任务结果: {result2}")
    except Exception as e:
        print(f"失败任务异常: {e}")
    
    # 检查任务状态
    print(f"成功任务是否完成: {task1.done()}")
    print(f"失败任务是否完成: {task2.done()}")
    print(f"失败任务异常: {task2.exception()}")
```

## Task 的超时处理

```python
async def task_timeout_demo():
    """演示 Task 的超时处理"""
    print("=== Task 超时处理演示 ===")
    
    async def slow_task(name, duration):
        """慢速任务"""
        print(f"{name} 开始执行")
        await asyncio.sleep(duration)
        print(f"{name} 完成")
        return f"{name} 的结果"
    
    # 创建慢速任务
    task = asyncio.create_task(slow_task("慢速任务", 5))
    
    try:
        # 设置超时时间
        result = await asyncio.wait_for(task, timeout=2.0)
        print(f"任务结果: {result}")
    except asyncio.TimeoutError:
        print("任务超时！")
        # 取消任务
        task.cancel()
        try:
            await task
        except asyncio.CancelledError:
            print("任务已被取消")
    
    print(f"任务状态: 完成={task.done()}, 取消={task.cancelled()}")
```

## 完整示例

```python
async def main():
    """主函数：演示 Task 的各种特性"""
    print("=== Task 对象完整演示 ===\n")
    
    # 1. 基本创建方法
    await basic_task_demo()
    
    # 2. 状态和属性
    await task_status_demo()
    
    # 3. 取消功能
    await task_cancellation_demo()
    
    # 4. 并发执行
    await concurrent_tasks_demo()
    
    # 5. 异常处理
    await task_exception_demo()
    
    # 6. 超时处理
    await task_timeout_demo()
    
    print("=== Task 总结 ===")
    print("1. Task 是对协程的包装")
    print("2. 可以使用 asyncio.create_task() 创建")
    print("3. Task 可以并发执行")
    print("4. Task 可以被取消")
    print("5. Task 有执行状态和异常信息")
    print("6. Task 支持超时处理")
    print("7. Task 是 asyncio 并发编程的核心")

if __name__ == "__main__":
    # 运行主协程
    asyncio.run(main())
```

## Task 总结

1. **Task 是对协程的包装**
2. **可以使用 asyncio.create_task() 创建**
3. **Task 可以并发执行**
4. **Task 可以被取消**
5. **Task 有执行状态和异常信息**
6. **Task 支持超时处理**
7. **Task 是 asyncio 并发编程的核心**

Task 对象是 asyncio 中最重要的概念之一，它提供了协程执行的高级控制功能。 