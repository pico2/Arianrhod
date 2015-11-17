from ml import *

def iterable(text):
    return text if isinstance(text, (list, tuple)) else [text]

def main():
    ed6_fc_text = json.loads(open('ed6_fc_text.json', 'rb').read().decode('utf-8-sig'))

    entries = []
    for text in ed6_fc_text:
        translation = text['translation']
        if not translation:
            continue

        rva = int(text['rva'], 16)
        entries.append((rva, translation))

    fs = fileio.FileStream('ed6fc.text', 'wb')
    fs.WriteULong(len(entries))

    for rva, text in entries:
        text = text.encode('gbk') + b'\x00'
        fs.WriteULong(rva)
        fs.WriteUShort(len(text))
        fs.Write(text)

    console.pause('done')

if __name__ == '__main__':
    Try(main)
