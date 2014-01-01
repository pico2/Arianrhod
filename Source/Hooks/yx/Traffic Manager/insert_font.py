from ml import *
import zlib, hashlib

tahoma9b_image_offset_offset = 0x323C355
tahoma9b_xml_offset_offset = 0x323C36A
append_data_offset = 0x323D300

def chhdr(buf, orig, comp, md5):
    return buf[:2] + struct.pack('<II', orig, comp) + buf[0xA:0x12] + md5 + buf[0x22:]

def main():
    asdb = BytesStream()
    asdb.open('traffic.asdb', 'rb+')

    tahoma9b_image_offset = 0xC

    tahoma9b_xml_offset = 0x5486

    asdb.seek(tahoma9b_image_offset)
    imghdr = asdb.read(0x2C)

    asdb.seek(tahoma9b_xml_offset)
    xmlhdr = asdb.read(0x2C)

    asdb.seek(append_data_offset)

    xml = open('font.xml', 'rb').read()
    img = open('font.bin', 'rb').read()

    xmlorig = len(xml)
    imgorig = len(img)

    xmlmd5 = hashlib.md5()
    xmlmd5.update(xml)
    xmlmd5 = xmlmd5.digest()

    imgmd5 = hashlib.md5()
    imgmd5.update(img)
    imgmd5 = imgmd5.digest()

    xml = zlib.compress(xml)
    img = zlib.compress(img)

    xmlhdr = chhdr(xmlhdr, xmlorig, len(xml), xmlmd5)
    imghdr = chhdr(imghdr, imgorig, len(img), imgmd5)

    asdb.seek(append_data_offset)

    xmloffset = append_data_offset

    asdb.write(xmlhdr)
    asdb.write(xml)

    round_up = 128

    imgoffset = asdb.tell()

    asdb.write(b'\x00' * (round_up - imgoffset % round_up))

    imgoffset = asdb.tell()

    asdb.write(imghdr)
    asdb.write(img)

    asdb.seek(tahoma9b_xml_offset_offset)
    asdb.wulong(xmloffset)

    asdb.seek(tahoma9b_image_offset_offset)
    asdb.wulong(imgoffset)

TryInvoke(main)

