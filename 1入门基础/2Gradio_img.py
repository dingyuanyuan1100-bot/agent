import gradio as gr
import cv2
import numpy as np


def reverse_img(img):
    #彩色图片转灰度图（PIL）
    gray_image = img.convert("L")
    #把PIL转为numpy数组（矩阵）
    gray_np = np.array(gray_image, dtype=np.float32)
    #图片反色
    inverted_image = 255.0 - gray_np
    #高斯模糊
    blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
    #对模糊后的图片再次反色
    inverted_blur = 255.0 - blurred
    # 防止除0，给分母加极小值
    pencil_sketch = cv2.divide(gray_np, inverted_blur, scale=256.0)
    #np.clip(val,0,255)：把所有像素限制在 0~255 之间。避免异常像素。astype(np.uint8)转回无符号 8 位整数， 正常显示图片。
    pencil_sketch = np.clip(pencil_sketch, 0, 255).astype(np.uint8)
    return pencil_sketch


demo = gr.Interface(
    fn=reverse_img,
    inputs=[gr.Image(label="上传图片", type="pil")],
    outputs=[gr.Image(label="铅笔画")],
    title="图片转铅笔画",
    description="将上传的图片转化为铅笔画。",
)

if __name__ == "__main__":
    demo.launch()
