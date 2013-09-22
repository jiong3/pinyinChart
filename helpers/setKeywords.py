import sys
import xml.etree.ElementTree as etree

PATH_IN_SVG = '../pinyinChartTrad.svg'
PATH_IN_TXT = 'keyword_list.txt'
PATH_OUT_SVG = '../pinyinChartEdit.svg'


with open(PATH_IN_TXT, mode='r', encoding='utf-8') as txt_file:
    keywords = [l.strip().split('\t') for l in txt_file.readlines()]

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

for i in range(0,len_han - 1):
    pinyin_list[i][0].text = keywords[i][0]
    keyword_list[i][0].text = keywords[i][1] + ' ' + keywords[i][3]
    hanzi_list[i][0].text = keywords[i][2]

pCsvg.write(PATH_OUT_SVG)
