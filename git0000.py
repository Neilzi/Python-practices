from PIL import Image, ImageDraw, ImageFont


def imageNum(img, num):
    imgNum = ImageDraw.Draw(img)
    w, h = img.size
    fillColor = "#ff0000"
    font = ImageFont.truetype("C:\Windows\Fonts\Arial.ttf", size=40)
    imgNum.text((w - 30, 5), num, fill=fillColor, font=font)
    img.show()
    return 0


if __name__ == "__main__":
    img = Image.open("thumbnail.png")
    imageNum(img, "3")