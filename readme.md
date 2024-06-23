# Image to SVG Converter

This is a simple tool written in Python that can convert an input image into SVG format. The tool utilizes the `vtracer` library for image conversion and the `Gradio` library to create a user-friendly web interface.

## Features

- Upload images and convert them to SVG format
- Support configuration of various conversion parameters, such as color mode, hierarchy, pattern, etc.
- The generated SVG file can be downloaded and saved, and previewed on the page

## Installation

First, make sure you have installed Python 3.7 or a higher version. Then, clone this project and install the dependencies:

```bash
git clone https://github.com/XueshuFun/vtracer-web-ui.git
cd vtracer-web-ui
pip install -r requirements.txt
```

## How to Use

Run the following command to start the Gradio interface:

```bash
python app.py
```

This will launch a local server and open a web page interface in your browser. In this interface, you can upload images and configure conversion parameters, and click the "Submit" button to generate and download the SVG file.

![](https://cdn.xueshu.fun/202406042142637.png)

## Parameter Explanation

- **Input Image**: Upload the image file you want to convert.
- **Color Mode**: Choose the color mode, which can be "Color" or "Monochrome".
- **Hierarchy**: Choose the hierarchy, which can be "Stack" or "Cut".
- **Mode**: Choose the conversion mode, which can be "Spline", "Polygon", or "None".
- **Filter Speckles**: Set the value for filtering speckles, ranging from 0 to 10.
- **Color Precision**: Set the value for color precision, ranging from 0 to 10.
- **Layer Difference**: Set the value for layer difference, ranging from 0 to 30.
- **Corner Threshold**: Set the value for corner threshold, ranging from 0 to 100.
- **Length Threshold**: Set the value for length threshold, ranging from 3.5 to 10.
- **Maximum Iterations**: Set the number of maximum iterations, ranging from 1 to 20.
- **Stitching Threshold**: Set the value for stitching threshold, ranging from 0 to 90.
- **Path Precision**: Set the value for path precision, ranging from 1 to 10.
