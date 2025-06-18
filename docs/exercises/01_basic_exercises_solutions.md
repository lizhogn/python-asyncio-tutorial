# 基础练习参考答案

## 练习 1：创建简单的协程

### 参考答案

```python
import asyncio

async def greet(name):
    """简单的协程函数，用于问候"""
    print(f"Hello, {name}!")
    await asyncio.sleep(1)  # 模拟异步操作
    print(f"Goodbye, {name}!")

async def main():
    """主函数"""
    print("开始执行协程...")
    await greet("Alice")
    await greet("Bob")
    print("所有协程执行完成！")

if __name__ == "__main__":
    asyncio.run(main())
```

### 运行结果
```
开始执行协程...
Hello, Alice!
Goodbye, Alice!
Hello, Bob!
Goodbye, Bob!
所有协程执行完成！
```

## 练习 2：并发执行协程

### 参考答案

```python
import asyncio
import time

async def task(name, duration):
    """模拟异步任务"""
    print(f"任务 {name} 开始执行...")
    await asyncio.sleep(duration)
    print(f"任务 {name} 完成！")
    return f"{name} 的结果"

async def main():
    """主函数 - 并发执行多个任务"""
    print("开始并发执行任务...")
    start_time = time.time()
    
    # 创建多个任务并发执行
    task1 = asyncio.create_task(task("A", 2))
    task2 = asyncio.create_task(task("B", 3))
    task3 = asyncio.create_task(task("C", 1))
    
    # 等待所有任务完成
    results = await asyncio.gather(task1, task2, task3)
    
    end_time = time.time()
    print(f"所有任务完成！总耗时: {end_time - start_time:.2f} 秒")
    print(f"结果: {results}")

if __name__ == "__main__":
    asyncio.run(main())
```

### 运行结果
```
开始并发执行任务...
任务 A 开始执行...
任务 B 开始执行...
任务 C 开始执行...
任务 C 完成！
任务 A 完成！
任务 B 完成！
所有任务完成！总耗时: 3.01 秒
结果: ['A 的结果', 'B 的结果', 'C 的结果']
```

## 练习 3：异步网络请求

### 参考答案

```python
import asyncio
import aiohttp
import time

async def fetch_url(session, url, name):
    """异步获取 URL 内容"""
    try:
        print(f"开始请求 {name}: {url}")
        async with session.get(url) as response:
            content = await response.text()
            print(f"{name} 请求完成，状态码: {response.status}")
            return f"{name}: {len(content)} 字符"
    except Exception as e:
        print(f"{name} 请求失败: {e}")
        return f"{name}: 请求失败"

async def main():
    """主函数 - 并发发送多个网络请求"""
    urls = [
        ("https://httpbin.org/delay/1", "请求1"),
        ("https://httpbin.org/delay/2", "请求2"),
        ("https://httpbin.org/delay/1", "请求3"),
    ]
    
    print("开始并发网络请求...")
    start_time = time.time()
    
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url, name) for url, name in urls]
        results = await asyncio.gather(*tasks)
    
    end_time = time.time()
    print(f"所有请求完成！总耗时: {end_time - start_time:.2f} 秒")
    print("结果:", results)

if __name__ == "__main__":
    asyncio.run(main())
```

### 运行结果
```
开始并发网络请求...
开始请求 请求1: https://httpbin.org/delay/1
开始请求 请求2: https://httpbin.org/delay/2
开始请求 请求3: https://httpbin.org/delay/1
请求1 请求完成，状态码: 200
请求3 请求完成，状态码: 200
请求2 请求完成，状态码: 200
所有请求完成！总耗时: 2.05 秒
结果: ['请求1: 374 字符', '请求2: 374 字符', '请求3: 374 字符']
```

## 练习 4：错误处理

### 参考答案

```python
import asyncio

async def risky_operation(name, should_fail=False):
    """可能失败的异步操作"""
    print(f"开始执行 {name}...")
    await asyncio.sleep(1)
    
    if should_fail:
        raise ValueError(f"{name} 操作失败！")
    
    print(f"{name} 执行成功！")
    return f"{name} 的结果"

async def main():
    """主函数 - 演示错误处理"""
    print("开始执行带错误处理的任务...")
    
    # 创建多个任务，其中一些会失败
    tasks = [
        asyncio.create_task(risky_operation("任务A", False)),
        asyncio.create_task(risky_operation("任务B", True)),
        asyncio.create_task(risky_operation("任务C", False)),
    ]
    
    # 使用 gather 收集结果，设置 return_exceptions=True
    results = await asyncio.gather(*tasks, return_exceptions=True)
    
    print("所有任务执行完成！")
    for i, result in enumerate(results):
        if isinstance(result, Exception):
            print(f"任务 {i+1} 失败: {result}")
        else:
            print(f"任务 {i+1} 成功: {result}")

if __name__ == "__main__":
    asyncio.run(main())
```

### 运行结果
```
开始执行带错误处理的任务...
开始执行 任务A...
开始执行 任务B...
开始执行 任务C...
任务A 执行成功！
任务B 操作失败！
任务C 执行成功！
所有任务执行完成！
任务 1 成功: 任务A 的结果
任务 2 失败: 任务B 操作失败！
任务 3 成功: 任务C 的结果
```

## 总结

这些练习涵盖了 asyncio 的基础用法：

1. **基本协程创建和执行**
2. **并发任务管理**
3. **异步网络请求**
4. **错误处理机制**

通过这些练习，你应该能够：
- 理解协程的基本概念
- 掌握 `async/await` 语法
- 学会使用 `asyncio.create_task()` 和 `asyncio.gather()`
- 了解异步编程的错误处理方式 