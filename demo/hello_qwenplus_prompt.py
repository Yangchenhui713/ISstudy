from http import HTTPStatus
import dashscope


def call_with_prompt():
    response = dashscope.Generation.call(
        model="qwen-plus-0723",
        prompt='请介绍一下通义千问'
    )
    # 如果调用成功，则打印模型的输出
    if response.status_code == HTTPStatus.OK:
        print(response)
    # 如果调用失败，则打印出错误码与失败信息
    else:
        print(response.code)  
        print(response.message) 

if __name__ == '__main__':
    call_with_prompt()