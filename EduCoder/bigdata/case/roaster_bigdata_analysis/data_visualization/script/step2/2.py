
from PIL import Image
def getDiff(width, high, image):  # 将要裁剪成w*h的image照片
    diff = []
    im = image.resize((width, high))
    imgray = im.convert('L')  # 转换为灰度图片 便于处理
    pixels = list(imgray.getdata())  # 得到像素数据 灰度0-255
    for row in range(high): # 逐一与它左边的像素点进行比较
        rowStart = row * width  # 起始位置行号
        for index in range(width - 1):
            leftIndex = rowStart + index
            rightIndex = leftIndex + 1  # 左右位置号
            diff.append(pixels[leftIndex] > pixels[rightIndex])
    return diff  #  *得到差异值序列 这里可以转换为hash码*
def getHamming(diff, diff2):  # 暴力计算两点间汉明距离
    hamming_distance = 0
    for i in range(len(diff)):
        if diff[i] != diff2[i]:
            hamming_distance += 1
    return hamming_distance

if __name__ == '__main__':

    a=Image.open("/data/workspace/myshixun/secret/step2/answer/factors_affecting_quality.png")
    b=Image.open("/data/workspace/myshixun/secret/step2/result/factors_affecting_quality.png")
    diff1 = getDiff(32, 32, a)
    diff2 = getDiff(32, 32, b)
    ans = getHamming(diff1, diff2)
    if ans < 1:
        print("图像对比一致，恭喜通关！")
    else:
        print("图像对比不一致，请检查你的代码")
