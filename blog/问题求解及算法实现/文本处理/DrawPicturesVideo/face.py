

import turtle
from PIL import Image,ImageDraw,ImageFont


# turtle.speed(5)
# turtle.setup(900, 600, 200, 200)
# turtle.pensize(5)
# turtle.right(90)
# turtle.penup()
# turtle.fd(100)
# turtle.left(90)
# turtle.pendown()
# turtle.begin_fill()
# turtle.pencolor("#B26A0F")  # head side color
# turtle.circle(150)
# turtle.fillcolor("#F9E549")  # face color
# turtle.end_fill()


img = Image.open(r"resources/static/bg.jpg")
jgz = Image.open(r"resources/static/ct.jpg")
img.paste(jgz,(63,46))
#控制表情的叠加位置
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("simyou.TTF",24)
draw.text((16,200),"Ahab杂货铺！", fill = (0,0,0), font = font)
#控制文字添加位置
img.show()
# img.save("生成的表情包.jpg")