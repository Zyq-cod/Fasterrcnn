from PIL import Image
import os
from xml.etree.ElementTree import Element, SubElement, tostring

# 定义一个函数来创建XML结构
def create_xml(image_info):
    root = Element('ImageInfo')
    for key, value in image_info.items():
        child = SubElement(root, key)
        child.text = str(value)
    return root

# 定义一个函数来处理单个图像文件
def process_image(file_path):
    with Image.open(file_path) as img:
        # 获取图像信息
        info = {
            'format': img.format,
            'size': img.size,
            'mode': img.mode
        }
        # 创建XML元素
        xml_root = create_xml(info)
        # 将XML元素转换为字符串
        xml_str = tostring(xml_root, encoding='unicode')
        # 返回XML字符串
        return xml_str

# 定义一个函数来批量处理文件夹中的所有JPG文件
def batch_process_images(input_folder, output_folder):
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    # 遍历输入文件夹中的所有文件
    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.jpg'):
            # 构建完整的文件路径
            file_path = os.path.join(input_folder, filename)
            # 处理图像并获取XML字符串
            xml_str = process_image(file_path)
            # 构建输出文件路径
            output_file_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.xml')
            # 将XML字符串保存到文件
            with open(output_file_path, 'w') as xml_file:
                xml_file.write(xml_str)

# 设置输入和输出文件夹路径
input_folder = 'image_folder/train_jpg'
output_folder = 'image_folder/labels'

# 调用函数批量处理图像
batch_process_images(input_folder, output_folder)