from os import getenv
from openai import OpenAI
import gradio as gr

openai_key = getenv("OPENAI_API_KEY")
messages=[]
use_moren={"role":"system","content":"You are a helpful assistant"}

client = OpenAI(
    api_key=openai_key,
    base_url="https://api.deepseek.com")
def open_ai(message, chat_history):
    if not openai_key:
        return "请配置环境"
    #chat_history 内容为 [{"role":"user", "content":"xxx"},{"role":"assistant", "content":"yyy"}]
    messages.extend(chat_history)
    messages.extend([use_moren,{"role":"user","content":message}])

    response = client.chat.completions.create(
        model="deepseek-flash",
        messages=messages,
        stream=False,
        reasoning_effort="low",
        extra_body={"thinking": {"type": "enabled"}}
        )
    return response.choices[0].message.content

demo = gr.ChatInterface(
    #ChatInterface不支持inputs和outputs
    fn=open_ai,
    title="deepseek_chat"
)
if __name__ == "__main__":
    demo.launch()
