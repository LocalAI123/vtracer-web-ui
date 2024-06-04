import gradio as gr
import vtracer
from PIL import Image
import io

def convert_image_to_svg(input_image, colormode='color', hierarchical='stacked', mode='spline', filter_speckle=4, color_precision=6, layer_difference=16, corner_threshold=60, length_threshold=4.0, max_iterations=10, splice_threshold=45, path_precision=3):
    # Convert the input image to SVG
    img = Image.open(input_image).convert('RGBA')
    pixels = list(img.getdata())
    size = img.size  # Get the size of the image
    svg_str = vtracer.convert_pixels_to_svg(pixels,
                                            size=size,
                                            colormode=colormode,
                                            hierarchical=hierarchical,
                                            mode=mode,
                                            filter_speckle=filter_speckle,
                                            color_precision=color_precision,
                                            layer_difference=layer_difference,
                                            corner_threshold=corner_threshold,
                                            length_threshold=length_threshold,
                                            max_iterations=max_iterations,
                                            splice_threshold=splice_threshold,
                                            path_precision=path_precision)
    
    # Save the SVG string to a file
    output_path = "output.svg"
    with open(output_path, "w") as f:
        f.write(svg_str)
    
    return output_path, svg_str

# Create Gradio Interface
interface = gr.Interface(
    fn=convert_image_to_svg,
    inputs=[
        gr.Image(type="file", label="输入图片"),
        gr.Radio(["彩色", "单色"], label="颜色模式", value="彩色"),
        gr.Radio(["堆叠", "剪切"], label="层次结构", value="堆叠"),
        gr.Radio(["样条", "多边形", "无"], label="模式", value="样条"),
        gr.Slider(0, 10, value=4, step=1, label="滤波斑点"),
        gr.Slider(0, 10, value=6, step=1, label="颜色精度"),
        gr.Slider(0, 30, value=16, step=1, label="层差"),
        gr.Slider(0, 100, value=60, step=1, label="角点阈值"),
        gr.Slider(3.5, 10, value=4.0, step=0.1, label="长度阈值"),
        gr.Slider(1, 20, value=10, step=1, label="最大迭代次数"),
        gr.Slider(0, 90, value=45, step=1, label="拼接阈值"),
        gr.Slider(1, 10, value=3, step=1, label="路径精度")
    ],
    outputs=[
        gr.File(label="下载SVG文件"),
        gr.HTML(label="SVG预览")
    ],
    title="图片转SVG转换器",
    description="上传一张图片并将其转换为SVG文件。"
)

# Launch the interface
if __name__ == "__main__":
    interface.launch()