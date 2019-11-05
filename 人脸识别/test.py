import cv2 as cv
import os
import sys
from PIL import Image
import numpy as np


# 读取图片
# img = cv.imread('../pillow/face.jpg')  # 路径中不可有中文
# # 显示图片
# cv.imshow('read_img', img)
# # 等待键盘输入
# cv.waitKey(0)  # 0无限等待
# # 释放空间
# cv.destroyAllWindows()

# 图片灰度
# img = cv.imread('../pillow/face.jpg')  # 路径中不可有中文
# # 显示图片
# cv.imshow('old_img', img)
# gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray_img', gray_img)
# cv.waitKey(0)
# cv.destroyAllWindows()
# # 保存图片
# cv.imwrite('gray_face.jpg', gray_img)


# 修改图片尺寸
# img = cv.imread('../pillow/face.jpg')  # 路径中不可有中文
# cv.imshow('old_img', img)
# print('原来图片的形状：', img.shape)
# img_resize = cv.resize(img, dsize=(200, 160))
# cv.imshow('img_resize', img_resize)
# print('现在图片的形状：', img_resize.shape)
#
# while True:
#     if ord('q') == cv.waitKey(0):
#         break
# cv.destroyAllWindows()

# 画图

# img = cv.imread('../pillow/face.jpg')
# # 画矩形
# x, y, w, h = 50, 50, 80, 80
# cv.rectangle(img, (x, y, x + w, y + h), color=(0, 255, 0), thickness=2)  # color = GBR
# cv.circle(img, (x + w // 2, y + h // 2), radius=w // 2, color=(0, 255, 0), thickness=2)  # color = GBR
# cv.imshow('result_img', img)
# cv.waitKey(0)
# cv.destroyAllWindows()

# 人脸检测（单个和多个）
# def face_detect_demo():
#     # 将图片转化为灰度图片
#     gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#     # 加载特征数据
#
#     face_detector = cv.CascadeClassifier(
#         'E:/python/opencv/sources/data/haarcascades/haarcascade_frontalface_default.xml')
#     # scaleFactor=1.03,minNeighbors=3,maxSize=(33,33),minSize=(27,27) 调整参数
#     faces = face_detector.detectMultiScale(gray)
#     for x, y, w, h in faces:
#         cv.rectangle(img, (x, y), (x + w, y + h), color=(0, 255, 0), thickness=2)
#         cv.circle(img, center=(x + w // 2, y + h // 2), radius=w // 2, color=(0, 255, 0), thickness=2)
#     cv.imshow('img', img)
#
#
# # 加载图片
# img = cv.imread('../pillow/face.jpg')
# face_detect_demo()
# # cv.imshow('img', img)
# cv.waitKey(0)
# cv.destroyAllWindows()

# 视频人脸检测
# def face_detect_demo(img):
#     # 将图片灰度
#     gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#     # 加载特征数据
#     face_detector = cv.CascadeClassifier(
#         'E:/python/opencv/sources/data/haarcascades/haarcascade_frontalface_default.xml')
#     faces = face_detector.detectMultiScale(gray)
#     for x, y, w, h in faces:
#         cv.rectangle(img, (x, y), (x + w, y + h), color=(0, 0, 255), thickness=2)
#         cv.circle(img, center=(x + w // 2, y + h // 2), radius=(w // 2), color=(0, 255, 0), thickness=2)
#     cv.imshow('result', img)
#
#
# video = cv.VideoCapture('video.mp4')
# while True:
#     flag, frame = video.read();
#     if not flag:
#         break
#     face_detect_demo(frame)
#     if ord('q') == cv.waitKey(0):
#         break
# cv.destroyAllWindows()
# video.release()

# 训练数据
def getImageAndLabels(path):
    facesSimple = []
    ids = []
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    # 检测人脸
    face_detector = cv.CascadeClassifier(
        'E:/python/opencv/sources/data/haarcascades/haarcascade_frontalface_default.xml')

    # print(imagePath)
    # 遍历列表中的图片
    for imagePath in imagePaths:
        # 打开图片
        PIL_img = Image.open(imagePath).convert('L')
        # 将图片转换为数组
        img_numpy = np.array(PIL_img, 'uint8')
        faces = face_detector.detectMultiScale(img_numpy)
        # 获取每张图片的id
        # print(os.path.split(imagePath))
        id = int(os.path.split(imagePath)[1].split('.')[0])
        for x, y, w, h in faces:
            facesSimple.append(img_numpy[y:y + h, x:w + x])
            ids.append(id)
    return facesSimple, ids


if __name__ == '__main__':
    pass
    # path = './jm'
    # # 获取图像数组和id标签数组
    # faces, ids = getImageAndLabels(path)
    # # 获取循环对象
    # recognizer = cv.face.LBPHFaceRecognizer_create()
    # recognizer.train(faces,np.array(ids))
    # # 保存文件
    # recognizer.write('trainer/trainer.yml')

# 人脸识别
# 加载训练数据集文件
recognizer = cv.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
# 准备识别的图片
img = cv.imread('3.pgm')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
face_detector = cv.CascadeClassifier(
    'E:/python/opencv/sources/data/haarcascades/haarcascade_frontalface_default.xml')
faces = face_detector.detectMultiScale(gray)
for x, y, w, h in faces:
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # 人脸识别
    id, confidence = recognizer.predict(gray[y:y + h, x:x + w])
    print('标签id:', id, '置信评分：', confidence)
cv.imshow('result', img)
cv.waitKey(0)
cv.destroyAllWindows()
