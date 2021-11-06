# -*- coding: utf-8 -*-

from PIL import Image, ImageFilter



def main():
    kitten = Image.open('https://github.com/REMitchell/python-scraping/blob/master/v2/files/textBad.png')
    blurryKitten = kitten.filter(ImageFilter.GaussianBlur)
    blurryKitten.save('kitten_blurred.jpg')
    blurryKitten.show()


if __name__ == "__main__":
    main()

