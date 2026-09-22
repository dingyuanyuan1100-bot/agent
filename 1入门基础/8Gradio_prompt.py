from openai import OpenAI
import gradio as gr
import os

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com")
def openai_deepseek_api(message, history,prompt):
    if not api_key:
        return "请配置环境"
    messages = []
    messages.extend(history)
    messages.extend([{"role": "system", "content":f"{prompt or "You are a helpful assistant"}"},{"role": "user", "content": f"{message}"}])

    response = client.chat.completions.create(
        model="deepseek-flash",
        messages=messages,
        stream=False,
        reasoning_effort="low",
        extra_body={"thinking": {"type": "enabled"}}
    )

    return response.choices[0].message.content

prompt = gr.Textbox(
        label="系统提示词",
        value="你是资深全栈开发工程师，回答简洁，代码附带注释，使用中文。",
        lines=3
    )

demo = gr.ChatInterface(
    openai_deepseek_api,
    #通过addtional_input增加参数
    additional_inputs=[prompt],
    title="DeepSeeK API",
    description="DeepSeeK API",
)

if __name__ == "__main__":
    demo.launch()