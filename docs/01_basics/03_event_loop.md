# 事件循环（Event Loop）

事件循环是 asyncio 的核心组件，它负责：
1. 管理和调度协程的执行
2. 处理 I/O 操作
3. 管理定时器
4. 处理系统信号

事件循环就像一个永不停止的循环，不断地检查是否有可以执行的任务。

## 获取当前事件循环

```python
import asyncio

def demonstrate_event_loop():
    """演示如何获取和使用事件循环"""
    print("=== 事件循环基础 ===")
    
    # 获取当前事件循环
    loop = asyncio.get_event_loop()
    print(f"当前事件循环: {loop}")
    print(f"事件循环是否运行: {loop.is_running()}")
    print(f"事件循环是否关闭: {loop.is_closed()}")
```

## 在事件循环中运行协程

```python
import asyncio
import time
from datetime import datetime

async def task_with_delay(name, delay):
    """带延迟的任务"""
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {name} 开始执行")
    await asyncio.sleep(delay)
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {name} 完成")
    return f"{name} 的结果"

async def demonstrate_loop_scheduling():
    """演示事件循环如何调度任务"""
    print("=== 事件循环调度演示 ===")
    
    # 创建多个任务
    tasks = [
        task_with_delay("任务A", 2),
        task_with_delay("任务B", 1),
        task_with_delay("任务C", 3),
    ]
    
    print("创建任务，开始执行...")
    start_time = time.time()
    
    # 并发执行所有任务
    results = await asyncio.gather(*tasks)
    
    end_time = time.time()
    print(f"所有任务完成，总耗时: {end_time - start_time:.2f} 秒")
    print(f"任务结果: {results}")
```

## 事件循环的不同运行方式

```python
async def demonstrate_loop_methods():
    """演示事件循环的不同运行方法"""
    print("=== 事件循环运行方法 ===")
    
    # 方法1: asyncio.run() (推荐)
    print("方法1: 使用 asyncio.run()")
    result1 = await task_with_delay("asyncio.run任务", 1)
    print(f"结果: {result1}")
    
    # 方法2: 手动获取循环并运行
    print("方法2: 手动获取循环")
    loop = asyncio.get_event_loop()
    if not loop.is_running():
        result2 = await task_with_delay("手动循环任务", 1)
        print(f"结果: {result2}")
```

## 事件循环中的定时器

```python
async def demonstrate_timers():
    """演示事件循环中的定时器功能"""
    print("=== 定时器演示 ===")
    
    async def periodic_task():
        """周期性任务"""
        for i in range(3):
            print(f"[{datetime.now().strftime('%H:%M:%S')}] 周期性任务 {i+1}/3")
            await asyncio.sleep(1)
    
    async def delayed_task():
        """延迟任务"""
        print(f"[{datetime.now().strftime('%H:%M:%S')}] 延迟任务开始")
        await asyncio.sleep(2)
        print(f"[{datetime.now().strftime('%H:%M:%S')}] 延迟任务完成")
    
    # 并发执行定时任务
    await asyncio.gather(periodic_task(), delayed_task())
```

## 事件循环的异常处理

```python
async def demonstrate_loop_exceptions():
    """演示事件循环中的异常处理"""
    print("=== 事件循环异常处理 ===")
    
    async def failing_task():
        """会失败的任务"""
        await asyncio.sleep(1)
        raise ValueError("任务执行失败")
    
    async def successful_task():
        """成功的任务"""
        await asyncio.sleep(0.5)
        return "任务成功"
    
    try:
        # 即使一个任务失败，其他任务仍会继续
        results = await asyncio.gather(
            successful_task(),
            failing_task(),
            successful_task(),
            return_exceptions=True  # 返回异常而不是抛出
        )
        
        for i, result in enumerate(results):
            if isinstance(result, Exception):
                print(f"任务 {i+1} 失败: {result}")
            else:
                print(f"任务 {i+1} 成功: {result}")
                
    except Exception as e:
        print(f"捕获到异常: {e}")
```

## 事件循环的性能监控

```python
async def demonstrate_loop_monitoring():
    """演示如何监控事件循环的性能"""
    print("=== 事件循环性能监控 ===")
    
    loop = asyncio.get_event_loop()
    
    # 记录开始时间
    start_time = time.time()
    
    # 执行一些任务
    tasks = [task_with_delay(f"监控任务{i}", 0.5) for i in range(5)]
    results = await asyncio.gather(*tasks)
    
    end_time = time.time()
    
    print(f"执行时间: {end_time - start_time:.2f} 秒")
    print(f"任务数量: {len(tasks)}")
    print(f"平均每个任务时间: {(end_time - start_time) / len(tasks):.2f} 秒")
```

## 事件循环的关闭和清理

```python
async def demonstrate_loop_cleanup():
    """演示事件循环的清理过程"""
    print("=== 事件循环清理 ===")
    
    async def cleanup_task():
        """清理任务"""
        print("执行清理任务...")
        await asyncio.sleep(1)
        print("清理任务完成")
    
    # 注册清理回调
    loop = asyncio.get_event_loop()
    loop.call_soon(lambda: print("事件循环即将关闭"))
    
    await cleanup_task()
    print("所有任务完成，事件循环可以安全关闭")
```

## 完整示例

```python
async def main():
    """主函数：演示事件循环的各种特性"""
    print("=== 事件循环完整演示 ===\n")
    
    # 1. 基础概念
    demonstrate_event_loop()
    
    # 2. 任务调度
    await demonstrate_loop_scheduling()
    
    # 3. 运行方法
    await demonstrate_loop_methods()
    
    # 4. 定时器
    await demonstrate_timers()
    
    # 5. 异常处理
    await demonstrate_loop_exceptions()
    
    # 6. 性能监控
    await demonstrate_loop_monitoring()
    
    # 7. 清理
    await demonstrate_loop_cleanup()
    
    print("=== 事件循环总结 ===")
    print("1. 事件循环是 asyncio 的核心调度器")
    print("2. 它管理所有协程的执行")
    print("3. 支持并发执行多个任务")
    print("4. 提供定时器和异常处理机制")
    print("5. 可以通过多种方式运行")
    print("6. 需要正确清理以避免资源泄漏")

if __name__ == "__main__":
    # 运行主协程
    asyncio.run(main())
```

## 事件循环总结

1. **事件循环是 asyncio 的核心调度器**
2. **它管理所有协程的执行**
3. **支持并发执行多个任务**
4. **提供定时器和异常处理机制**
5. **可以通过多种方式运行**
6. **需要正确清理以避免资源泄漏**

事件循环是异步编程的心脏，理解它的工作原理对于掌握 asyncio 至关重要。 