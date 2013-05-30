import struct

def BuildBmpHeader(width, height, bpp):
    stride = (int(width * bpp / 8) + 3) & ~3
    size = stride * height + 0x36
    header = struct.pack('<HIIIIIIHHIIIIII', 0x4D42, size, 0, 0x36, 0x28, width, height, 1, bpp, 0, 0, 0, 0, 0, 0)
    return header

