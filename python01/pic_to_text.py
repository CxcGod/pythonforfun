# by Andy
# encoding=utf-8

from PIL import Image


# 字符集，从最黑到空白，以图片的灰度值来判断,灰度值越高，越白，使用的字符越靠后


img_file='example.png'
HEIGHT=51
WIDTH=51
out_file='example.txt'

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
length=len(ascii_char)
def get_char(r,g,b,alpha = 256):
    if alpha==0:
        return ' '
    #从RGB向灰度值转变
    gray=int(0.2126*r+0.7152*g+0.0722*b)
    #注意小心溢出
    n=(256.0+1)/length
    return ascii_char[int(gray/n)]

img=Image.open(img_file)
#压缩转换按照所给的大小
img=img.resize((WIDTH,HEIGHT),Image.NEAREST)

txt=""

for i in range(HEIGHT):
    for j in range(WIDTH):
        txt += get_char(*img.getpixel((j,i)))
    txt +='\n'
print(txt)

with open(out_file,'w') as f:
    f.write(txt)