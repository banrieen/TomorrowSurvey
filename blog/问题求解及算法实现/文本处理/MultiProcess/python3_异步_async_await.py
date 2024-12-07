""" Python3 协程实现
协程通过 async/await 语法进行声明，是编写异步应用的推荐方式。
"""

import asyncio
import time

""" 
# asyncio.run() 函数用来运行最高层级的入口点 "main()" 函数,
# 等待一个协程。以下代码段会在等待 1 秒后打印 "hello"，然后 再次 等待 2 秒后打印 "world",
# asyncio.create_task() 函数用来并发运行作为 asyncio 任务 的多个协程。
 """
async def say_after(delay, what):
    await asyncio.sleep(delay)
    print("You say: %s " % what)

async def main_queen():
    print(f"Start at {time.strftime('%X')}")
    await say_after(1, 'hello')
    await say_after(2, 'world')
    print(f"Finished at {time.strftime('%X')}")

async def main():
    # 将协程创建为任务，可并行执行
    task1 = asyncio.create_task(say_after(1,"Hello "))
    task2 = asyncio.create_task(say_after(2, "World !"))
    print(f"Start at {time.strftime('%X')}")
    await task1
    await task2
    print(f"Finished at {time.strftime('%X')}")
    
# 协程对象为可等待的
# 可等待 对象有三种主要类型: asyc 协程, task 任务 和 Future.
async def nested():
    return 42

async def async_object():
    nested()
    print(await nested())
    task1 = asyncio.create_task(nested())
    print("Await task: ")
    await task1

""" Future 是一种特殊的 低层级 可等待对象，表示一个异步操作的 最终结果。

当一个 Future 对象 被等待，这意味着协程将保持等待直到该 Future 对象在其他地方操作完毕。

在 asyncio 中需要 Future 对象以便允许通过 async/await 使用基于回调的代码。

通常情况下 没有必要 在应用层级的代码中创建 Future 对象。

Future 对象有时会由库和某些 asyncio API 暴露给用户，用作可等待对象:
 """
async def main():
    await function_that_returns_a_future_object()
    # this is also valid:
    await asyncio.gather(
        function_that_returns_a_future_object(),
        some_python_coroutine()
    )

# 基于生成器的协程

@asyncio.coroutine
def old_style_coroutine():
    print("HAHAHAHA......")
    yield from asyncio.sleep(1)

async def neW_style_coroutine():
    print("HAHAHAHA......")
    await asyncio.sleep(3600)

async def old_main():
    # flag  = asyncio.iscoroutine(old_style_coroutine())
    # print(flag)
    # print(asyncio.iscoroutinefunction(old_style_coroutine()))
    try:
        # await old_style_coroutine()
        asyncio.wait_for(neW_style_coroutine(),timeout=1.5)
    except asyncio.TimeoutError:
        raise TimeoutError("Timeout !")

# 并发运行任务
mget, mset

async def factorial(name, number):
    f = 1 
    for i in range(2, number+1):
        print(f"Task {name}: Compute factorial({i}).... ")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: Factorial({number}) = {f}")

async def new_main():
    await asyncio.gather(
        factorial("Tom", 4),
        factorial("Jack", 8),
        factorial("Tomas", 16),

    )

# asyncio.run(main())
# asyncio.run(async_object())
asyncio.run(new_main())