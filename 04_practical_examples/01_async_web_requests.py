"""
04_practical_examples/01_async_web_requests.py

异步网络请求示例

这个示例展示了如何使用 asyncio 进行高效的网络请求。
我们将对比同步和异步的网络请求方式，展示异步编程的优势。
"""

import asyncio
import aiohttp
import requests
import time
from datetime import datetime


# 1. 同步网络请求（对比用）
def sync_fetch_url(session, url):
    """同步获取URL内容"""
    try:
        response = session.get(url, timeout=10)
        response.raise_for_status()
        return {
            'url': url,
            'status': response.status_code,
            'size': len(response.content),
            'time': time.time()
        }
    except Exception as e:
        return {
            'url': url,
            'error': str(e),
            'time': time.time()
        }


def sync_fetch_multiple_urls(urls):
    """同步获取多个URL"""
    print("=== 同步网络请求演示 ===")
    start_time = time.time()
    
    with requests.Session() as session:
        results = []
        for url in urls:
            print(f"正在请求: {url}")
            result = sync_fetch_url(session, url)
            results.append(result)
            print(f"完成: {url} - 状态: {result.get('status', 'ERROR')}")
    
    end_time = time.time()
    print(f"同步请求总耗时: {end_time - start_time:.2f} 秒")
    print(f"成功请求数: {len([r for r in results if 'status' in r])}")
    print()
    return results


# 2. 异步网络请求
async def async_fetch_url(session, url):
    """异步获取URL内容"""
    try:
        async with session.get(url, timeout=10) as response:
            content = await response.read()
            return {
                'url': url,
                'status': response.status,
                'size': len(content),
                'time': time.time()
            }
    except Exception as e:
        return {
            'url': url,
            'error': str(e),
            'time': time.time()
        }


async def async_fetch_multiple_urls(urls):
    """异步获取多个URL"""
    print("=== 异步网络请求演示 ===")
    start_time = time.time()
    
    async with aiohttp.ClientSession() as session:
        # 创建所有请求任务
        tasks = [async_fetch_url(session, url) for url in urls]
        
        # 并发执行所有请求
        results = await asyncio.gather(*tasks)
        
        # 按完成顺序显示结果
        for result in results:
            status = result.get('status', 'ERROR')
            print(f"完成: {result['url']} - 状态: {status}")
    
    end_time = time.time()
    print(f"异步请求总耗时: {end_time - start_time:.2f} 秒")
    print(f"成功请求数: {len([r for r in results if 'status' in r])}")
    print()
    return results


# 3. 带进度显示的异步请求
async def async_fetch_with_progress(urls):
    """带进度显示的异步请求"""
    print("=== 带进度的异步请求演示 ===")
    start_time = time.time()
    
    async def fetch_with_progress(session, url, index, total):
        """带进度显示的单个请求"""
        print(f"[{index+1}/{total}] 开始请求: {url}")
        result = await async_fetch_url(session, url)
        print(f"[{index+1}/{total}] 完成: {url} - 状态: {result.get('status', 'ERROR')}")
        return result
    
    async with aiohttp.ClientSession() as session:
        tasks = [
            fetch_with_progress(session, url, i, len(urls))
            for i, url in enumerate(urls)
        ]
        results = await asyncio.gather(*tasks)
    
    end_time = time.time()
    print(f"带进度异步请求总耗时: {end_time - start_time:.2f} 秒")
    print()
    return results


# 4. 限制并发数的异步请求
async def async_fetch_with_semaphore(urls, max_concurrent=3):
    """限制并发数的异步请求"""
    print(f"=== 限制并发数({max_concurrent})的异步请求演示 ===")
    start_time = time.time()
    
    # 创建信号量来限制并发数
    semaphore = asyncio.Semaphore(max_concurrent)
    
    async def fetch_with_semaphore(session, url):
        """使用信号量限制并发的请求"""
        async with semaphore:
            print(f"开始请求: {url}")
            result = await async_fetch_url(session, url)
            print(f"完成: {url} - 状态: {result.get('status', 'ERROR')}")
            return result
    
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_with_semaphore(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
    
    end_time = time.time()
    print(f"限制并发异步请求总耗时: {end_time - start_time:.2f} 秒")
    print()
    return results


# 5. 带超时的异步请求
async def async_fetch_with_timeout(urls, timeout=5):
    """带超时的异步请求"""
    print(f"=== 带超时({timeout}秒)的异步请求演示 ===")
    start_time = time.time()
    
    async def fetch_with_timeout(session, url):
        """带超时的单个请求"""
        try:
            result = await asyncio.wait_for(
                async_fetch_url(session, url),
                timeout=timeout
            )
            print(f"完成: {url} - 状态: {result.get('status', 'ERROR')}")
            return result
        except asyncio.TimeoutError:
            print(f"超时: {url}")
            return {
                'url': url,
                'error': 'Timeout',
                'time': time.time()
            }
    
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_with_timeout(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
    
    end_time = time.time()
    print(f"带超时异步请求总耗时: {end_time - start_time:.2f} 秒")
    print()
    return results


# 6. 错误处理和重试机制
async def async_fetch_with_retry(urls, max_retries=3):
    """带重试机制的异步请求"""
    print(f"=== 带重试机制({max_retries}次)的异步请求演示 ===")
    start_time = time.time()
    
    async def fetch_with_retry(session, url):
        """带重试的单个请求"""
        for attempt in range(max_retries + 1):
            try:
                result = await async_fetch_url(session, url)
                if 'status' in result and result['status'] == 200:
                    print(f"成功: {url} (尝试 {attempt + 1})")
                    return result
                else:
                    print(f"失败: {url} (尝试 {attempt + 1}) - {result.get('error', 'Unknown error')}")
            except Exception as e:
                print(f"异常: {url} (尝试 {attempt + 1}) - {e}")
            
            if attempt < max_retries:
                await asyncio.sleep(1)  # 等待1秒后重试
        
        return {
            'url': url,
            'error': f'Failed after {max_retries + 1} attempts',
            'time': time.time()
        }
    
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_with_retry(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
    
    end_time = time.time()
    print(f"带重试异步请求总耗时: {end_time - start_time:.2f} 秒")
    print()
    return results


async def main():
    """主函数：演示各种异步网络请求方式"""
    # 测试URL列表
    test_urls = [
        'https://httpbin.org/delay/1',
        'https://httpbin.org/delay/2',
        'https://httpbin.org/delay/1',
        'https://httpbin.org/status/200',
        'https://httpbin.org/status/404',
        'https://httpbin.org/status/500',
        'https://httpbin.org/bytes/1024',
        'https://httpbin.org/json',
    ]
    
    print("=== 异步网络请求完整演示 ===\n")
    
    # 1. 同步请求（对比）
    sync_results = sync_fetch_multiple_urls(test_urls[:3])  # 只测试前3个
    
    # 2. 基本异步请求
    async_results = await async_fetch_multiple_urls(test_urls)
    
    # 3. 带进度的异步请求
    progress_results = await async_fetch_with_progress(test_urls[:4])
    
    # 4. 限制并发数的异步请求
    semaphore_results = await async_fetch_with_semaphore(test_urls, max_concurrent=2)
    
    # 5. 带超时的异步请求
    timeout_results = await async_fetch_with_timeout(test_urls, timeout=3)
    
    # 6. 带重试的异步请求
    retry_results = await async_fetch_with_retry(test_urls[:3], max_retries=2)
    
    print("=== 性能对比总结 ===")
    print("同步请求: 按顺序执行，总时间 = 所有请求时间之和")
    print("异步请求: 并发执行，总时间 ≈ 最长的单个请求时间")
    print("异步编程在网络请求中能显著提升性能！")


if __name__ == "__main__":
    # 运行主协程
    asyncio.run(main()) 