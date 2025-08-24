import openai

openai.api_key = '你的API_KEY'

def ai_chat(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "你是一个有帮助的AI助手。"},
            {"role": "user", "content": user_input},
        ]
    )
    return response['choices'][0]['message']['content']

print("欢迎来到AI聊天！输入'再见'结束。")
while True:
    msg = input("你说: ")
    if msg == '再见':
        print("AI: 再见！")
        break
    reply = ai_chat(msg)
    print("AI:", reply)