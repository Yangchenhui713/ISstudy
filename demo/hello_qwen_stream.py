from http import HTTPStatus
from dashscope import Generation


def call_with_stream():
    messages = [
        {'role':'system','content':'you are a helpful assistant'},
        {'role': 'user','content': '三国演义中的曹操和三国志中的曹操以及东汉史中的曹操有什么不同？'}
        ]
    responses = Generation.call(
        model="qwen-plus-0723",
        messages=messages,
        # 设置输出为'message'格式
        result_format='message',
        # 设置输出方式为流式输出
        stream=True,
        # 增量式流式输出
        incremental_output=True
        )
    full_content = ""
    for response in responses:
        if response.status_code == HTTPStatus.OK:
            print(response)
            full_content += response.output.choices[0].message.content
        else:
            print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
                response.request_id, response.status_code,
                response.code, response.message
            ))
    print(f"Full content:{full_content}")

if __name__ == '__main__':
    call_with_stream()