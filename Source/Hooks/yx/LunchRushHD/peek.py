from ml import *

def main(file):
    workbook = ET.parse(file).getroot()

    xmlns = '{urn:schemas-microsoft-com:office:spreadsheet}'

    xml = XMLCreate()

    for sheet in workbook.findall(xmlns + 'Worksheet'):
        name = sheet.attrib[xmlns + 'Name']
        SetConsoleTitle(name)

        for table in sheet.findall(xmlns + 'Table'):

            rows = table.findall(xmlns + 'Row')
            for row in rows[1:]:
                cells = row.findall(xmlns + 'Cell')
                if len(cells) < 3:
                    continue

                #if len(cells[0].attrib) != 0: continue

                data0 = cells[0].find(xmlns + 'Data')
                if data0 == None:
                    continue

                if data0.attrib[xmlns + 'Type'] != 'String':
                    bp()

                if data0.find('_') == -1:
                    bp()

                data1 = cells[1].find(xmlns + 'Data')
                if data1 == None:
                    continue

                data0 = data0.text
                data1 = data1.text

                print(data0)

                XMLAppendText(xml, data1, 'Workbook="%s" Id="%s"' % (name, data0))

    XMLSaveTo(xml, file + '.xml')

TryInvoke(main, 'strings.xml')
