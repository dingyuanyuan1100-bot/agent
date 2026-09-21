import gradio as gr
from openai import OpenAI
import os
def open_ai(content):
    #环境变量配置 $env:DEEPSEEK_API_KEY="key"  py 脚本.py
    open_key = os.getenv("DEEPSEEK_API_KEY")
    #deepseek官方配置
    client = OpenAI(
        api_key=open_key,
        base_url="https://api.deepseek.com")

    response = client.chat.completions.create(
        model="deepseek-flash",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": f"{content}"},
        ],
        stream=False,
        reasoning_effort="low",
        extra_body={"thinking": {"type": "enabled"}}
    )
    print(content)
    return response.choices[0].message.content


demo = gr.Interface(
    fn=open_ai,
    inputs=["text"],
    outputs=["text"],
    title="deepseek",
)
if __name__ == "__main__":
    demo.launch()