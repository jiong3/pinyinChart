import sys
import xml.etree.ElementTree as etree

PATH_IN_SVG = '../pinyinChartTrad.svg'
PATH_OUT_TXT = 'keyword_list.txt'

pCsvg = etree.parse(PATH_IN_SVG)
root = pCsvg.getroot()


hanzi_list = root[4]
pinyin_list = root[5]
keyword_list = root[6]

len_han = len(hanzi_list)
len_pin = len(pinyin_list)
len_key = len(keyword_list)

if not (len(set((len_han, len_pin, len_key))) == 1):
    sys.exit('error in file')

output_file = []
for i in range(0,len_han - 1):
    display = pinyin_list[i][0].text+'\t'
    display += keyword_list[i][0].text[0]+'\t'
    display += hanzi_list[i][0].text+'\t'
    display += keyword_list[i][0].text[2:]
    output_file.append(display)

with open(PATH_OUT_TXT, mode='w', encoding='utf-8') as txt_file:
    txt_file.write('\n'.join(output_file))

