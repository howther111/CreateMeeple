import cv2
import numpy as np
from PIL import Image, ImageDraw

def createMeeple(red=127, green=127, blue=127):
    # 600 x 600 の4レイヤー(BGRA)を定義
    size = (1000, 1000)
    img = Image.new("RGBA", size, color=(0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.ellipse((300, 50, 700, 450), fill=(red, green, blue))
    draw.polygon(((100, 400), (100, 600), (900, 600), (900, 400)), fill=(red, green, blue))
    draw.polygon(((400, 500), (400, 700), (600, 700), (600, 500)), fill=(red, green, blue))
    draw.polygon(((400, 550), (100, 950), (400, 950), (500, 600)), fill=(red, green, blue))
    draw.polygon(((600, 550), (900, 950), (600, 950), (500, 600)), fill=(red, green, blue))
    # 画像の表示
    fileName = "MeepleR" + str(red) + "G" + str(green) + "B" + str(blue) + ".png"
    img.save(fileName, quality=100)