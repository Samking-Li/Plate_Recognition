# -*- coding: utf-8 -*-

import cv2
import numpy as np
import json
import time
import pytesseract
import matplotlib.pyplot as plt

class TesPlateRecognition():
    pytesseract.pytesseract.tesseract_cmd = 'H:/Program Files/Tesseract-OCR/tesseract.exe'

    def __init__(self):
        self.MAX_WIDTH = 1000  # 原始图片最大宽度
        self.Min_Area = 2000  # 车牌区域允许最大面积
        self.PROVINCE_START = 1000

        # 省份代码保存在provinces.json中
        with open('provinces.json', 'r', encoding='utf-8') as f:
            self.provinces = json.load(f)

        # 车牌类型保存在cardtype.json中，便于调整
        with open('cardtype.json', 'r', encoding='utf-8') as f:
            self.cardtype = json.load(f)

        # 字母所代表的地区保存在Prefecture.json中，便于更新
        with open('Prefecture.json', 'r', encoding='utf-8') as f:
            self.Prefecture = json.load(f)

        # 车牌识别的部分参数保存在js中，便于根据图片分辨率做调整
        f = open('config.js')
        j = json.load(f)
        for c in j["config"]:
            if c["open"]:
                self.cfg = c.copy()
                break
    def __del__(self):
        pass

    def plt_showfullcolor(self, img):
        b, g, r = cv2.split(img)
        img = cv2.merge([r, g, b])
        plt.imshow(img)
        plt.show()

    def plt_showgray(self, img):
        plt.imshow(img, cmap='gray')
        plt.show()

    def imreadex(self, filename):
        image = cv2.imdecode(np.fromfile(filename, dtype=np.uint8), cv2.IMREAD_COLOR)
        return image

    def gray_guss(self, img):
        img = cv2.GaussianBlur(img, (3, 3), 0)
        gray_image = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        return gray_image

    def plate_cut(self, path):
        img = self.imreadex(path)
        gray_image = self.gray_guss(img)
        # x方向上的边缘检测（增强边缘信息）
        Sobel_x = cv2.Sobel(gray_image, cv2.CV_16S, 1, 0)
        absX = cv2.convertScaleAbs(Sobel_x)
        image = absX
        # 图像阈值化操作——获得二值化图
        ret, image = cv2.threshold(image, 0, 255, cv2.THRESH_OTSU)
        # 腐蚀（erode）和膨胀（dilate）
        kernelX = cv2.getStructuringElement(cv2.MORPH_RECT, (35, 1))
        # x方向进行闭操作（抑制暗细节）
        image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernelX)
        # y方向开操作去除小连通
        kernelY = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 30))
        image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernelY)
        image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernelY)
        # 中值滤波（去噪）
        image = cv2.medianBlur(image, 21)
        # 获得轮廓
        contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for item in contours:
            rect = cv2.boundingRect(item)
            x = rect[0]
            y = rect[1]
            weight = rect[2]
            height = rect[3]
            # 根据轮廓的形状特点，确定车牌的轮廓位置并截取图像
            if (weight > (height * 3)) and (weight < (height * 4)):
                image = img[y:y + height, x:x + weight]

        #颜色识别
        green = yellow = blue = black = white = 0
        try:
            # 有转换失败的可能，原因来自于上面矫正矩形出错
            image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        except:
            print('未发现车牌区域')
            image = color = None
            return image, color

        row_num, col_num = image_hsv.shape[:2]
        image_count = row_num * col_num
        for i in range(row_num):
                for j in range(col_num):
                    H = image_hsv.item(i, j, 0)
                    S = image_hsv.item(i, j, 1)
                    V = image_hsv.item(i, j, 2)
                    if 11 < H <= 34 and S > 34:  # 图片分辨率调整
                        yellow += 1
                    elif 35 < H <= 99 and S > 34:  # 图片分辨率调整
                        green += 1
                    elif 99 < H <= 124 and S > 34:  # 图片分辨率调整
                        blue += 1
                    if 0 < H < 180 and 0 < S < 255 and 0 < V < 46:
                        black += 1
                    elif 0 < H < 180 and 0 < S < 43 and 221 < V < 225:
                        white += 1
        color = "no"

        if yellow * 3 >= image_count:
            color = "黄色牌照"
        elif green * 3 >= image_count:
            color = "绿色牌照"
        elif blue * 3 >= image_count:
            color = "蓝色牌照"
        elif black + white >= image_count * 0.7:
            color = "bw"
        return image, color

    def TesOCR(self, img, color):
        result= {}
        errpic = cv2.imread('err.jpg')
        try:
            img = self.gray_guss(img)
            image = np.zeros_like(img)
        except:
            result['InputTime'] = time.strftime("%Y-%m-%d %H:%M:%S")
            result['Type'] = '无法识别'
            result['Picture'] = errpic
            result['Number'] = '无法识别'
            result['From'] = '未知'
            return result
        cv2.normalize(img, image, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
        ret, image = cv2.threshold(image, 200, 255, cv2.THRESH_BINARY)
        kernelX = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 1))
        # 进行闭操作（抑制暗细节）
        image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernelX)
        license_result = pytesseract.image_to_string(image, lang='chi_sim+eng',config="--psm 7 plate",)
        if license_result !='':
            result['InputTime'] = time.strftime("%Y-%m-%d %H:%M:%S")
            result['Type'] = color
            result['Picture'] = img
            result['Number'] = ''.join(license_result[:2]) + '·' + ''.join(license_result[2:])
            try:
                result['From'] = ''.join(self.Prefecture[license_result[0]][license_result[1]])
            except:
                result['From'] = '未知'
            return result
        else:
            print('未能识别')
            return None


# 测试
if __name__ == '__main__':
    c = TesPlateRecognition()
    img, color = c.plate_cut('temp.jpg')
    result = c.TesOCR(img, color)
    print(result)
    #cv2.imshow('card', card_imgs)

    #cv2.waitKey(0)
