"""
第 0000 题：
将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。

PIL (Python Imaging Library ) 
http://pillow.readthedocs.io/en/3.1.x/index.html
"""

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

img = Image.open("test.png")
draw = ImageDraw.Draw(img)

# font = ImageFont.truetype(<font-file>, <font-size>)
font = ImageFont.truetype("arial.ttf", 16) 

# draw.text((x, y),"Sample Text",(r,g,b)) position, text contents, color, font
# img.size: tuple of img.size
# xy – Top left corner of the text.
draw.text((img.size[0]-img.size[0]*0.2, 0),"5",(255,255,255),font=font)


img.save('sample-out.png')

