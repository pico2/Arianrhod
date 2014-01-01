#encoding=utf-8

from ml import *
import sqlite3

def main():
    conn = sqlite3.connect('locale.db')
    c = conn.cursor()

    c.execute('select * from tblLocale')

    text = []
    for x in c.fetchall():
        if x[0] == '' or x[1] == '':
            continue
        text.append('%s' % x[0])

    open('text.txt', 'wb').write('\r\n'.join(text).encode('U16'))

TryInvoke(main)
