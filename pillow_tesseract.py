#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image, ImageFilter

kitten = Image.open('https://github.com/REMitchell/python-scraping/blob/master/v2/files/textBad.png')
blurryKitten = kitten.filter(ImageFilter.GaussianBlur)
blurryKitten.save('kitten_blurred.jpg')
blurryKitten.show()




