import cv2 as cv

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

img = cv.imread('../pillow/face.jpg')
# 画矩形
x, y, w, h = 50, 50, 80, 80
cv.rectangle(img, (x, y, x + w, y + h), color=(0, 255, 0), thickness=2)  # color = GBR
cv.circle(img, (x + w // 2, y + h // 2), radius=w // 2, color=(0, 255, 0), thickness=2)  # color = GBR
cv.imshow('result_img', img)
cv.waitKey(0)
cv.destroyAllWindows()
