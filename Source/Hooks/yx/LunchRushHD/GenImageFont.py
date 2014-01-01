from ml import *
import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

def GenerateImageFont(saveto, charlist, fontfile, fontsize, textrgb = None):

    if type(charlist) == str:
        charlist = list(charlist)

    charlist = list(sorted(set(charlist)))
    textrgb = tuple(textrgb) if textrgb != None else (0, 0, 0)

    font = ImageFont.truetype(fontfile, fontsize)
    draw = ImageDraw.Draw(Image.new("RGBA", (fontsize, fontsize), (255, 255, 255)))

    maxsize = [0, 0]

    for ch in charlist:
        size = draw.textsize(ch, font = font)
        if size[0] > maxsize[0]:
            maxsize = size

    maxsize = list(maxsize)
    w, h = maxsize
    h += 10

    imgsize = 256
    while imgsize * imgsize <= len(charlist) * w * h:
        imgsize *= 2

    img = Image.new("RGBA", (imgsize, imgsize), (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)

    xml = XMLCreate(RootTag = 'ImageFont', attrib = 'Width="%d" Height="%d"' % (imgsize, imgsize))

    rbf = BytesStream().open('font.rbf', 'wb')
    rbf.write(b'TFBR')
    rbf.wushort(len(charlist))

    x, y = 0, 0
    for ch in charlist:
        chrw, chrh = draw.textsize(ch, font = font)
        xcenter, ycenter = x + (w - chrw) / 2, y + (h - chrh) / 2
        draw.text((xcenter, ycenter), ch, textrgb, font = font)

        xml.append('    <char id="0x%X" left="%d" top="%d" right="%d" bottom="%d" x="%d" y="%d" width="%d" height="%d" />' % 
            (ord(ch), x, y, x + w, y + h, xcenter, ycenter, chrw, chrh)
        )

        id      = ord(ch)
        left    = float(x) / imgsize
        top     = float(y) / imgsize
        right   = float(x + w) / imgsize
        bottom  = float(y + h) / imgsize
        width   = float(chrw) / imgsize

        rbf.write(struct.pack('<Hfffff', id, left, top, right, bottom, width))

        x += w
        if x + w >= imgsize:
            y += h
            x = 0

    XMLSaveTo(xml, saveto + '.xml', RootTag = 'ImageFont')
    img.save(saveto + '.png')

def main():
    charlist = '中文en静音'
    GenerateImageFont('SimHei46_page0', charlist, 'simhei.ttf', 46, (93, 125, 148))

TryInvoke(main)
