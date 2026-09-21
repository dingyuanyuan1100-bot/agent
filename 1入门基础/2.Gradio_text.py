"""
Gradio为机器学习提供可以快速部署的web和deno
类似的 如 ChatGLM2-6B,gpt_academic,stavle-diffusion-webui

"""
import gettext

import gradio as gr

#功能实现
def reverse_text(text):
    number = len(text)
    return text[::-1] , number

demo = gr.Interface(
    fn = reverse_text,  #调用该函数
    inputs = ["text"],  #输入为文字

    outputs = ["text","number"], #输出为文本
    title = "文本处理工具",#设置页面标题
    description="输入一段文字，查看其倒序形式及字符数",
    examples=[["hi"],["world"]]

)
demo.launch()