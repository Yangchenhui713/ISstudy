from dashscope import Generation

def get_response(messages):
    response = Generation.call(model="qwen-plus-0723",
                               messages=messages,
                               # 将输出设置为"message"格式
                               result_format='message')
    return response


messages = [{'role': 'system', 'content': 'You are a helpful assistant.'}]

# 您可以自定义设置对话轮数，当前为3
for i in range(10):
    user_input = input("请输入：")
    # 将用户问题信息添加到messages列表中
    messages.append({'role': 'user', 'content': user_input})
    assistant_output = get_response(messages).output.choices[0]['message']['content']
    # 将大模型的回复信息添加到messages列表中
    messages.append({'role': 'assistant', 'content': assistant_output})
    print(f'用户输入：{user_input}')
    print(f'模型输出：{assistant_output}')
    print('\n')