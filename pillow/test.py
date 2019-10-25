from PIL import Image, ImageEnhance, ImageDraw, ImageFont
from PIL import ImageFile
from PIL import ImageFilter
from PIL import ImageChops
import random
import numpy as np
import os
import pickle

# 打开图片
ImageFile.LOAD_TRUNCATED_IMAGES = True
# im = Image.open('face.jpg').convert(mode='RGB')
# im2 = Image.new('RGB', im.size, 'red')
# # im2.show()
# Image.blend(im, im2, alpha=0.5).show()  # 透明度混合

# im1 = Image.open('face.jpg')
# im2 = Image.open('bb.jpg')
# im2 = im2.resize(im1.size)
# # print(im2.split())
# r, g, b = im2.split()
# Image.composite(im2, im1, b).show()  # 遮罩混合

# img = Image.open('face.jpg')
# img.show()
# 将每个像素扩大二倍
# Image.eval(img, lambda x: x * 2).show()

# 按尺寸进行缩放图片
# 复制图片
# img2 = img.copy()
# # img.show()
# img2.thumbnail((100, 80))
# img2.show()

# 剪切粘贴
# img1 = img.copy()
# img2 = img.copy()
#
# img_crop = img1.crop((10, 10, 150, 150))
# img2.paste(img_crop, (30, 30))
# img2.show()

# 图像旋转
# img.rotate(180).show()  # 旋转180度

# 格式转换
# img.transpose(Image.FLIP_TOP_BOTTOM).show()  # 上下滤镜
# img.transpose(Image.FLIP_LEFT_RIGHT).show()  # 左右滤镜
# img.transpose(Image.ROTATE_90).show()
# img.transpose(Image.ROTATE_180).show()
# img.transpose(Image.ROTATE_270).show()
# img.transpose(Image.TRANSPOSE).show()

# 分离和合并
# img2 = Image.open('bb.jpg')
# img2 = img2.resize(img.size)
# # 分离
# r1, g1, b1 = img.split()
# r2, g2, b2 = img2.split()
#
# temp = [r1, g2, b1]
# img3 = Image.merge('RGB', temp)
# img3.show()

# 滤镜
# 创建img
# w, h = img.size
# img_output = Image.new('RGB', (2 * w, h))
# img_output.paste(img, (0, 0))
# img_filter = img.filter(ImageFilter.GaussianBlur)  # 高斯模糊
# img_filter2 = img.filter(ImageFilter.EDGE_ENHANCE)  # 边缘增强
# img_filter3 = img.filter(ImageFilter.FIND_EDGES)  # 寻找边缘
# filters = []
# filters.append(img_filter)
# filters.append(img_filter2)
# filters.append(img_filter3)
# for i in filters:
#     img_output.paste(i, (w, 0))
#     img_output.show()

# 图片合成
# img2 = Image.open('bb.jpg')
# 对两张图片进行算术加法运算
# ImageChops.add(img, img2).show()
# 对两张图片进行算术减法运算
# ImageChops.subtract(img,img2).show()
# 使用Darker
# ImageChops.darker(img, img2).show()

# lighter
# ImageChops.lighter(img, img2).show()
# 两张图片相互叠加
# ImageChops.multiply(img, img2).show()
# screen
# ImageChops.screen(img, img2).show()

# 反色
# ImageChops.invert(img).show()
# 比较函数
# ImageChops.difference(img,img2).show()

# 图像色彩，亮度调整
# w, h = img.size
# img_output = Image.new('RGB', (3 * w, h))
# img_output.paste(img, (0, 0))
# 获取色彩调整器对象
# img_color = ImageEnhance.Color(img)
# imgb = img_color.enhance(1.5)  # 大于1 是增强
# img_bright = ImageEnhance.Brightness(img)
# imgb = img_bright.enhance(1.5)
# img_output.paste(imgb, (w, 0))
# imgc = img_bright.enhance(0.3)  # 小于1 是减弱
# img_output.paste(imgc, (2 * w, 0))
# img_output.show()

# 像素点进行变亮变暗
# w, h = img.size
# img_output = Image.new('RGB', (3 * w, h))
# img_output.paste(img, (0, 0))
# imgb = img.point(lambda x: x * 1.4)
# imgc = img.point(lambda x: x * 0.4)
# img_output.paste(imgb, ( w, 0))
# img_output.paste(imgc, (2* w, 0))
# img_output.show()


# # 显示图片
# # im.show()
# print('图片的格式：', im.format)
# print('图片的大小：', im.size)
# print('图片的高度：', im.height)
# print('图片的宽度：', im.width)
# print('获取（100,100）的像素值：', im.getpixel((100,100)))


# 创建一副白色背景的图像
# img = Image.new('RGB', (300, 200), 'white')
#
# # 绘制矩形
# draw_obj = ImageDraw.Draw(img)
# draw_obj.rectangle((50, 50, 150, 150), outline='red', fill='blue')
# font = ImageFont.truetype('方正粗黑宋简体.ttf', 20)
# draw_obj.text((50, 50), text='你好，你好', fill='white', font=font)
# img.show()

# 绘制圆
# img = Image.open('bb.jpg')
# w, h = img.size
# img_draw = ImageDraw.Draw(img)
# img_draw.arc((0, 0, h - 1, h - 1), 0, 360, fill='blue')
# img.save('circle.jpg')

# ImageFont
# img = Image.open('face.jpg')
# draw_obj = ImageDraw.Draw(img)
# font = ImageFont.load_default()
# font = ImageFont.truetype('方正粗黑宋简体.ttf', 20)
#
# draw_obj.text((30, 10), text='你好，你好', font=font, fill='white')
# font = ImageFont.truetype(r'C:\Windows\Fonts\微软雅黑\msyhbd.ttc', 20)
# draw_obj.text((30, 40), text='你好，你好', font=font, fill='white')
# img.show()

# 绘制十字
# img = Image.open('face.jpg')
# draw_obj = ImageDraw.Draw(img)
# w, h = img.size
# draw_obj.line((0, 0, w, h), fill=(255, 255, 0), width=3)
# draw_obj.line((0, h, w, 0), fill=(255, 255, 0), width=3)
# img.show()

# 绘制验证码

# width = 100
# height = 100
#
# im = Image.new('RGB', (width, height), (255, 255, 255))
# draw_obj = ImageDraw.Draw(im)
#
#
# def get_color():
#     return random.randint(200, 255), random.randint(200, 255), random.randint(200, 255)
#
#
# def get_char():
#     return chr(random.randint(65, 97))
#
#
# for x in range(width):
#     for y in range(height):
#         draw_obj.point((x, y), fill=get_color())
#
# font = ImageFont.truetype('方正粗黑宋简体.ttf', 20)
#
# # 绘制随机字母
# for i in range(4):
#     draw_obj.text((20 * i + 10, 40), get_char(), fill=(255, 0, 0), font=font)
#
# draw_obj.line((10, 10, 80, 80), fill='green', width=3)
# im.show()

# 绘制九宫格
# width, height = 300, 300
#
# img = Image.new('RGB', (width, height), (255, 255, 255))
# draw_obj = ImageDraw.Draw(img)
#
#
# def get_color(x, y):
#     a = x // 100 + y // 100
#     if a == 0:
#         return 255, 0, 0
#     elif a == 1:
#         return 255, 255, 0
#     elif a == 2:
#         return 255, 255, 255
#     elif a == 3:
#         return 0, 0, 255
#     elif a == 4:
#         return 0, 255, 255
#     else:
#         return 0, 0, 0
#
# for x in range(width):
#     for y in range(height):
#         draw_obj.point((x, y), fill=get_color(x, y))
# img.show()

# 改变图中的颜色
# img = Image.open('bb.jpg')
# w, h = img.size
# draw_obj = ImageDraw.Draw(img)
#
#
# def get_color(old_color):
#     if old_color[0] > 60 and old_color[1] > 60:
#         return old_color[0], 0, old_color[2]
#     else:
#         return old_color
#
#
# for x in range(w):
#     for y in range(h):
#         old_color = img.getpixel((x, y))
#         draw_obj.point((x, y), fill=get_color(old_color))
#
# img.show()


# 读取图片
# 读取图片的目录
image_dir = './images/'
# 保存图片的目录
result_dir = './result/'
# 保存数组的文件
array_file = './array.bin'


# 读取images目录下的图片，将图片保存成大的一维数组，将数组保存到文件
def image_to_array_file():
    # 获取图片名称
    filenames = os.listdir(image_dir)
    image_arrs = np.array([])
    for file in filenames:
        img = Image.open(image_dir + file)
        r, g, b = img.split()

        # 将r g b 转换为一维的数组

        r_arr = np.array(r).reshape(62500)
        g_arr = np.array(g).reshape(-1)
        b_arr = np.array(b).reshape(62500)

        # 将 r_arr  g_arr  b_arr 拼接为一维数组
        arrs = np.concatenate((r_arr, g_arr, b_arr))
        image_arrs = np.concatenate((arrs, image_arrs))

    # 将一维数组保存到文件中
    with open(array_file, 'wb') as f:
        pickle.dump(image_arrs, f)


# 读取文件中的内容
def file_to_image():
    with open(array_file, 'rb') as f:
        images = pickle.load(f)

        # 一维数组中 8,3,250,250 8张图片 3个通道 250*250 的图片
        image_arr = images.reshape((8, 3, 250, 250))
        for i in range(8):
            r = Image.fromarray(image_arr[i][0]).convert('L')
            g = Image.fromarray(image_arr[i][1]).convert('L')
            b = Image.fromarray(image_arr[i][2]).convert('L')

            # 合并图片
            image = Image.merge('RGB', (r, g, b))
            image.save(result_dir + str(i) + '.jpg')


if __name__ == '__main__':
    file_to_image()
    pass
    # image_to_array_file()
