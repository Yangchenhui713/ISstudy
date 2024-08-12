import asyncio
import platform
from dashscope.aigc.generation import AioGeneration

# 定义异步任务列表
async def task(question):
    try:
        print(f"Sending question: {question}")
        response = await AioGeneration.call("qwen-plus-0723",
                                            prompt=question)
        print(f"Received answer: {response.output.text}")
    except Exception as e:
        print(f"Error processing question '{question}': {e}")

# 主异步函数
async def main():
    questions = ["你是谁？", "你会什么？", "天气怎么样？"]
    tasks = [task(q) for q in questions]
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    # 设置事件循环策略
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    # 运行主协程
    try:
        asyncio.run(main(), debug=False)
    except Exception as e:
        print(f"An error occurred: {e}")